function readFrameData( data, frameTime, bone ) {

    // end sites have no motion data
    if ( bone.type === "ENDSITE" ) {

        return;

    }

    // add keyframe
    var keyframe = {
        time: frameTime,
        position: { x: 0, y: 0, z: 0 },
        rotation: new THREE.Quaternion(),
    };

    bone.frames.push( keyframe );
    var quat = new THREE.Quaternion();

    var vx = new THREE.Vector3( 1, 0, 0 );
    var vy = new THREE.Vector3( 0, 1, 0 );
    var vz = new THREE.Vector3( 0, 0, 1 );

    // parse values for each channel in node
    for ( var i = 0; i < bone.channels.length; ++ i ) {

        switch ( bone.channels[ i ] ) {

        case "Xposition":
            keyframe.position.x = parseFloat( data.shift().trim() );
            break;
        case "Yposition":
            keyframe.position.y = parseFloat( data.shift().trim() );
            break;
        case "Zposition":
            keyframe.position.z = parseFloat( data.shift().trim() );
            break;
        case "Xrotation":
            quat.setFromAxisAngle( vx, parseFloat( data.shift().trim() ) * Math.PI / 180 );
            keyframe.rotation.multiply( quat );
            break;
        case "Yrotation":
            quat.setFromAxisAngle( vy, parseFloat( data.shift().trim() ) * Math.PI / 180 );
            keyframe.rotation.multiply( quat );
            break;
        case "Zrotation":
            quat.setFromAxisAngle( vz, parseFloat( data.shift().trim() ) * Math.PI / 180 );
            keyframe.rotation.multiply( quat );
            break;
        default:
            throw "invalid channel type";

        }

    }

    // parse child nodes
    for ( var i = 0; i < bone.children.length; ++ i ) {

        readFrameData( data, frameTime, bone.children[ i ] );

    }

}
function toTHREEAnimation(roots) {
    var tracks = [];
    var bones = roots;
    // create a position and quaternion animation track for each node
    for ( var i = 0; i < bones.length; ++ i ) {

        var bone = bones[ i ];

        if ( bone.type == "ENDSITE" )
            continue;

        // track data
        var times = [];
        var positions = [];
        var rotations = [];

        // for ( var j = 0; j < bone.frames.length; ++ j ) {
        var frame = bone.frames[ bone.frames.length-1 ];
        times.push( frame.time );

        // the animation system animates the position property,
        // so we have to add the joint offset to all values
        positions.push( frame.position.x + bone.offset.x );
        positions.push( frame.position.y + bone.offset.y );
        positions.push( frame.position.z + bone.offset.z );

        rotations.push( frame.rotation.x );
        rotations.push( frame.rotation.y );
        rotations.push( frame.rotation.z );
        rotations.push( frame.rotation.w );

        // }

        if ( true ) {

            tracks.push( new THREE.VectorKeyframeTrack(
                ".bones[" + bone.name + "].position", times, positions ) );

        }

        if ( true ) {

            tracks.push( new THREE.QuaternionKeyframeTrack(
                ".bones[" + bone.name + "].quaternion", times, rotations ) );

        }

    }

    return new THREE.AnimationClip( "animation", - 1, tracks );

}

var clock = new THREE.Clock();

var camera, controls, scene, renderer;
var mixer = [];
var skeletonHelper = [];
var boneContainer = [];
var skeleton = [];
var bvh_header = [];
var root = [];
var frametime_combo = [];
init();
animate();
var loader = new THREE.BVHLoader();
var frametime_combo1 = 0
var total_skeleton = 20;
var socket_last_digit =2;
bvh_header[0]='';
const socket= [];
var socket_collected=0;
var socket_connected =[];
connectSockets()
//initialize websockets
// for( i =0 ; i< 20 ; i++){
//     bvh_header[i] = '';
//     frametime_combo[i]= 0
//     root[i] =0
//     if(i<8){
//         socket[i]= new WebSocket('ws://127.0.0.1:500'+ (socket_last_digit+i));
//     }else{
//         socket[i]= new WebSocket('ws://127.0.0.1:50'+ (socket_last_digit+i));
//     }
//     try {
//         socket[i].addEventListener('open', function(event) {
//             console.log(event.currentTarget.url)
//         });
//         socket[i].addEventListener('close', function(event) {
//             console.log(event.currentTarget.url)
//         });
//       } catch (error) {
//         console.log(i)
//         // listenSocket(k)
//       }
   
// }
console.log(socket)

// loop for multiple sockets to listen 


function listenSocket(k){
   
    socket[k].addEventListener('message', function(event) {
        getData (k,event);
        
    });
}

//visulize socket data 
function getData (i ,event){
    
    if(bvh_header[i] == ''){
        //header data 
        bvh_header[i] = event.data ;
        loader.load( bvh_header[i], function( result ){
            root[i] = result.root;
            skeletonHelper[i] = new THREE.SkeletonHelper( result.skeleton.bones[ 0 ] );
            skeletonHelper[i].skeleton = result.skeleton;
            skeletonHelper[i].material.linewidth = 5;
            boneContainer[i] = new THREE.Group();
            boneContainer[i].add( result.skeleton.bones[ 0 ] );
            scene.add( skeletonHelper[i] );
            scene.add( boneContainer[i] );
        });
        
    }else{
        // motion data 
        frametime_combo[i]+=0.01666
        var motion_data = event.data.split(' ')
        readFrameData(motion_data,frametime_combo[i],root[i][0 ])
        var threeClip = toTHREEAnimation(root[i])
        mixer[i] = new THREE.AnimationMixer( skeletonHelper[i] );
        mixer[i].clipAction( threeClip ).setEffectiveWeight( 1.0 ).play();
        
    }
}
function init() {

    camera = new THREE.PerspectiveCamera( 60, window.innerWidth / window.innerHeight, 10, 100000 );
    camera.position.set( 0, 2000, 5000 );
    controls = new THREE.OrbitControls( camera );
    controls.minDistance = 10;
    controls.maxDistance = 10000;

    scene = new THREE.Scene();
    scene.position.y= -480;
    scene.add( new THREE.GridHelper( 20000, 100 ) );

    // renderer
    renderer = new THREE.WebGLRenderer( { antialias: true } );
    renderer.setClearColor( 0xeeeeee );
    renderer.setPixelRatio( window.devicePixelRatio );
    renderer.setSize( window.innerWidth, window.innerHeight );

    document.body.appendChild( renderer.domElement );

    window.addEventListener( 'resize', onWindowResize, false );

}

function onWindowResize() {

    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();

    renderer.setSize( window.innerWidth, window.innerHeight );

}

function animate() {

    requestAnimationFrame( animate );

    var delta = clock.getDelta();
    // loop for all skeletons 
    for( i =0 ; i< total_skeleton ; i++){
        if ( mixer[i] ) mixer[i].update( delta );
        if ( skeletonHelper [i]) skeletonHelper[i].update();
    }
    renderer.render( scene, camera );

}


function connectSockets(){
    for( i =0 ; i< 20 ; i++){
        var socket_url = 'ws://127.0.0.1:500'+ (socket_last_digit+i);
        if(! socket_connected.includes(socket_url)){
            if(socket_collected == 0){
                bvh_header[i] = '';
                frametime_combo[i]= 0
                root[i] =0
            }
            if(i<8){
                socket[i]= new WebSocket('ws://127.0.0.1:500'+ (socket_last_digit+i));
            }else{
                socket[i]= new WebSocket('ws://127.0.0.1:50'+ (socket_last_digit+i));
            }
            
            socket[i].addEventListener('open', function(event) {
                socket_connected.push(event.currentTarget.url)
            });
            socket[i].addEventListener('close', function(event) {
                console.log(event.currentTarget.url)
            });
          
        }
    }
    socket_collected =1;
    for(k=0; k<total_skeleton ; k++){
        listenSocket(k)
    }
}


setInterval(connectSockets, 15000);
