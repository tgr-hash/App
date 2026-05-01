# 👾 Games

**DO NOT USE THIS AT SCHOOL.**  
**Disclosure: All of the games listed below were made partially with the use of Large Language Models such as ChatGPT or Copilot.**  
**Available games:**  
**Breakout**  
**Platforms**  
**Two player pong**  
**Singleplayer Pong**  
**Flappy Bird (now with full pixelart)**  
**Snake**  
**Block game (dino game with blocks)**  
**Aim trainer**  
**Dodge**  
**Maze Runner**  
**Fruit Ninja**  
**Mini Shooter (Galactica)**  
**Sandbox Circle**  
**What games should I make next?**  
**U should make color by number lol**

\<a\> href=”[https://url](https://url)”\>display text\</a\>

Flappy bird   
javascript:(function()%7Bif(document.getElementById(%22fB%22))return%3Bvar%20c=document.createElement(%22canvas%22)%3Bc.id=%22fB%22%3Bc.width=400%3Bc.height=600%3BObject.assign(c.style%2C%7Bposition%3A%22fixed%22%2Cleft%3A%2250%25%22%2Ctop%3A%2250%25%22%2Ctransform%3A%22translate(-50%25%2C-50%25)%22%2CzIndex%3A999999999%2Cborder%3A%224px%20solid%20%23333%22%2CborderRadius%3A%2210px%22%7D)%3Bdocument.body.appendChild(c)%3Bvar%20x=c.getContext(%222d%22)%3Bvar%20ball=%7Bx%3A80%2Cy%3A300%2Cv%3A0%2Cr%3A12%7D%3Bvar%20pipes=%5B%5D%3Bvar%20frame=0%3Bvar%20gravity=0.45%3Bvar%20jump=-7.5%3Bvar%20gameOver=false%3Bvar%20score=0%3Bvar%20highScore=0%3Bvar%20colors=%5B%22%232ecc71%22%2C%22%233498db%22%2C%22%239b59b6%22%2C%22%23e67e22%22%2C%22%23e74c3c%22%5D%3Bfunction%20pipeColor()%7Breturn%20colors%5BMath.floor(score/20)%25colors.length%5D%7Dfunction%20addPipe()%7Bvar%20h=Math.random()\*250+50%3Bpipes.push(%7Bx%3A400%2Ctop%3Ah%2Cbot%3Ah+150%2Cscored%3Afalse%7D)%7Dfunction%20reset()%7Bball.y=300%3Bball.v=0%3Bpipes=%5B%5D%3Bframe=0%3Bscore=0%3BgameOver=false%7Dfunction%20update()%7Bif(gameOver)return%3Bball.v%2B=gravity%3Bball.y%2B=ball.v%3Bif(ball.y%3C0%7C%7Cball.y%3Ec.height)%7BgameOver=true%3BhighScore=Math.max(highScore%2Cscore)%7Dif(frame%2590===0)addPipe()%3Bpipes.forEach(p%3D%3E%7Bp.x-=%202%3Bif(ball.x+ball.r%3Ep.x%26%26ball.x-ball.r%3Cp.x+50%26%26(ball.y-ball.r%3Cp.top%7C%7Cball.y+ball.r%3Ep.bot))%7BgameOver=true%3BhighScore=Math.max(highScore%2Cscore)%7Dif(\!p.scored%26%26p.x+50%3Cball.x)%7Bp.scored=true%3Bscore++%7D%7D)%3Bpipes=pipes.filter(p%3D%3Ep.x\>-50)%3Bframe++%7Dfunction%20draw()%7Bx.fillStyle=%22%2370c5ce%22%3Bx.fillRect(0%2C0%2Cc.width%2Cc.height)%3Bx.fillStyle=%22yellow%22%3Bx.beginPath()%3Bx.arc(ball.x%2Cball.y%2Cball.r%2C0%2C2\*Math.PI)%3Bx.fill()%3Bpipes.forEach(p%3D%3E%7Bx.fillStyle=pipeColor()%3Bx.fillRect(p.x%2C0%2C50%2Cp.top)%3Bx.fillRect(p.x%2Cp.bot%2C50%2Cc.height-p.bot)%7D)%3Bx.fillStyle=%22%23000%22%3Bx.font=%2220px%20sans-serif%22%3Bx.fillText(%22Score:%22+score%2C20%2C30)%3Bx.fillText(%22High:%22+highScore%2C320%2C30)%3Bif(gameOver)%7Bx.fillStyle=%22red%22%3Bx.font=%2230px%20sans-serif%22%3Bx.fillText(%22GAME%20OVER%22%2C90%2C300)%3Bx.font=%2216px%20sans-serif%22%3Bx.fillText(%22Click/Space/R%20Restart%22%2C65%2C330)%3Bx.fillText(%22ESC%20Quit%22%2C145%2C355)%7D%7Dfunction%20loop()%7Bupdate()%3Bdraw()%3BrequestAnimationFrame(loop)%7Dfunction%20flap()%7Bif(gameOver)reset()%3Bball.v=jump%7Dfunction%20keyHandler(e)%7Bif(e.code===%22Space%22)flap()%3Bif(e.key.toLowerCase()===%22r%22)reset()%3Bif(e.code===%22Escape%22)%7Bc.remove()%3Bdocument.removeEventListener(%22keydown%22%2CkeyHandler)%7D%7Ddocument.addEventListener(%22keydown%22%2CkeyHandler)%3Bc.addEventListener(%22click%22%2Cflap)%3Bloop()%7D)()

Maze Runner  
javascript:(function(){if(document.getElementById("fB"))return;var c=document.createElement("canvas");c.id="fB";c.width=400;c.height=400;Object.assign(c.style,{position:"fixed",left:"50%",top:"50%",transform:"translate(-50%,-50%)",zIndex:999999999,border:"4px solid \#333",borderRadius:"10px"});document.body.appendChild(c);var x=c.getContext("2d"),rows=10,cols=10,cellSize=c.width/cols,maze=\[\],visited=\[\],dirs=\[\[0,-1\],\[1,0\],\[0,1\],\[-1,0\]\];for(var y=0;y\<rows;y++){maze\[y\]=\[\];visited\[y\]=\[\];for(var x2=0;x2\<cols;x2++){maze\[y\]\[x2\]=\[1,1,1,1\];visited\[y\]\[x2\]=false;}}function genMaze(cx,cy){visited\[cy\]\[cx\]=true;var d=dirs.slice().sort(()=\>Math.random()-0.5);for(var i=0;i\<d.length;i++){var dx=d\[i\]\[0\],dy=d\[i\]\[1\],nx=cx+dx,ny=cy+dy;if(nx\>=0&\&nx\<cols&\&ny\>=0&\&ny\<rows&&\!visited\[ny\]\[nx\]){if(dx===1){maze\[cy\]\[cx\]\[1\]=0;maze\[ny\]\[nx\]\[3\]=0;}if(dx===-1){maze\[cy\]\[cx\]\[3\]=0;maze\[ny\]\[nx\]\[1\]=0;}if(dy===1){maze\[cy\]\[cx\]\[2\]=0;maze\[ny\]\[nx\]\[0\]=0;}if(dy===-1){maze\[cy\]\[cx\]\[0\]=0;maze\[ny\]\[nx\]\[2\]=0;}genMaze(nx,ny);}}}genMaze(0,0);var player={x:0,y:0},exit={x:cols-1,y:rows-1};function draw(){x.fillStyle="\#fff";x.fillRect(0,0,c.width,c.height);x.strokeStyle="\#000";x.lineWidth=2;for(var y=0;y\<rows;y++){for(var x2=0;x2\<cols;x2++){var cell=maze\[y\]\[x2\],px=x2\*cellSize,py=y\*cellSize;if(cell\[0\]){x.beginPath();x.moveTo(px,py);x.lineTo(px+cellSize,py);x.stroke();}if(cell\[1\]){x.beginPath();x.moveTo(px+cellSize,py);x.lineTo(px+cellSize,py+cellSize);x.stroke();}if(cell\[2\]){x.beginPath();x.moveTo(px+cellSize,py+cellSize);x.lineTo(px,py+cellSize);x.stroke();}if(cell\[3\]){x.beginPath();x.moveTo(px,py+cellSize);x.lineTo(px,py);x.stroke();}}}x.fillStyle="green";x.fillRect(exit.x\*cellSize+cellSize/4,exit.y\*cellSize+cellSize/4,cellSize/2,cellSize/2);x.fillStyle="red";x.fillRect(player.x\*cellSize+cellSize/4,player.y\*cellSize+cellSize/4,cellSize/2,cellSize/2);}draw();function move(dx,dy){var cell=maze\[player.y\]\[player.x\];if(dx===1&\&cell\[1\]===0)player.x+=1;if(dx===-1&\&cell\[3\]===0)player.x-=1;if(dy===1&\&cell\[2\]===0)player.y+=1;if(dy===-1&\&cell\[0\]===0)player.y-=1;draw();if(player.x===exit.x&\&player.y===exit.y){setTimeout(()=\>{alert("You reached the exit\!");c.remove();},10);}}function keyHandler(e){if(e.code==="ArrowUp")move(0,-1);if(e.code==="ArrowDown")move(0,1);if(e.code==="ArrowLeft")move(-1,0);if(e.code==="ArrowRight")move(1,0);if(e.code==="Escape")c.remove();}document.addEventListener("keydown",keyHandler);})();

Dodge game  
javascript:(()=\>{if(document.getElementById("dodgeGame"))return;const c=document.createElement("canvas");c.id="dodgeGame";c.width=400;c.height=400;Object.assign(c.style,{position:"fixed",left:"50%",top:"50%",transform:"translate(-50%,-50%)",zIndex:999999999,border:"4px solid \#333",borderRadius:"10px",background:"\#fff"});document.body.appendChild(c);const x=c.getContext("2d");let p,o,s,g,b=2,t,r=\!0;function S(){clearInterval(t);t=setInterval(()=\>{g||O()},200)}function R(){p={x:170,y:340,width:25,height:25};o=\[\];s=0;g=\!1;S()}function O(){const w=Math.random()\*35+17.5,h=Math.random()\*30+10,X=Math.random()\*(c.width-w);o.push({x:X,y:-h,width:w,height:h})}function M(d){p.x+=d;p.x\<0&&(p.x=0);p.x+p.width\>c.width&&(p.x=c.width-p.width)}function K(e){if(\!r)return;("a"===e.key||"ArrowLeft"===e.key)&\&M(-25);("d"===e.key||"ArrowRight"===e.key)&\&M(25);("r"===e.key||"R"===e.key)&&(R(),requestAnimationFrame(U));"Escape"===e.key&\&C()}function C(){r=\!1;clearInterval(t);document.removeEventListener("keydown",K);c.remove()}function U(){if(\!r||g)return;x.clearRect(0,0,c.width,c.height);const v=b+.05\*s;for(let i=o.length-1;i\>=0;i--){const a=o\[i\];a.y+=v;x.fillStyle="black";x.fillRect(a.x,a.y,a.width,a.height);a.y+a.height\>p.y&\&a.y\<p.y+p.height&\&a.x+a.width\>p.x&\&a.x\<p.x+p.width&&(g=\!0);a.y\>c.height&&(o.splice(i,1),s++)}x.fillStyle="red";x.fillRect(p.x,p.y,p.width,p.height);x.fillStyle="black";x.font="20px sans-serif";x.fillText("Score: "+s,10,25);g?(x.fillStyle="red",x.font="30px sans-serif",x.fillText("GAME OVER",95,200),x.font="16px sans-serif",x.fillText("R \= Restart   ESC \= Quit",90,230)):requestAnimationFrame(U)}document.addEventListener("keydown",K);R();requestAnimationFrame(U)})();

Aim trainer  
javascript:(()=\>{"use strict";if(document.getElementById("clickDotsGame"))return;const c=document.createElement("canvas");c.id="clickDotsGame";c.width=800;c.height=600;Object.assign(c.style,{position:"fixed",left:"50%",top:"50%",transform:"translate(-50%,-50%)",zIndex:999999999,border:"4px solid \#333",borderRadius:"10px",background:"\#111"});document.body.appendChild(c);const ctx=c.getContext("2d");let dots=\[\],score=0,running=\!0,GAME\_TIME=3e4,startTime=Date.now();function spawnDot(){const s=Math.random()\*20+30;const X=Math.random()\*(c.width-s);const Y=Math.random()\*(c.height-s);dots.push({x:X,y:Y,size:s,created:Date.now(),lifespan:1e3+2e3\*Math.random()})}function draw(){if(\!running)return;const now=Date.now(),elapsed=now-startTime;ctx.fillStyle="\#111";ctx.fillRect(0,0,c.width,c.height);dots=dots.filter(d=\>now-d.created\<d.lifespan);ctx.fillStyle="\#a0dfff";dots.forEach(d=\>{ctx.beginPath();ctx.arc(d.x+d.size/2,d.y+d.size/2,d.size/2,0,2\*Math.PI);ctx.fill()});ctx.fillStyle="white";ctx.font="20px sans-serif";ctx.fillText("Score: "+score,10,25);ctx.fillText("Time: "+Math.max(0,Math.ceil((GAME\_TIME-elapsed)/1e3))+"s",10,50);if(elapsed\>=GAME\_TIME){running=\!1;ctx.fillStyle="yellow";ctx.font="30px sans-serif";ctx.fillText("TIME'S UP\! Final Score: "+score,200,300);return}requestAnimationFrame(draw)}function clickHandler(e){if(\!running)return;const r=c.getBoundingClientRect(),mx=e.clientX-r.left,my=e.clientY-r.top;for(let i=dots.length-1;i\>=0;i--){const d=dots\[i\],dx=mx-(d.x+d.size/2),dy=my-(d.y+d.size/2);if(Math.sqrt(dx\*dx+dy\*dy)\<=d.size/2){score++;dots.splice(i,1);break}}}function keyHandler(e){if(e.key==="Escape"){running=\!1;document.removeEventListener("keydown",keyHandler);document.removeEventListener("click",clickHandler);c.remove()}if(e.key==="r"||e.key==="R"){dots=\[\];score=0;running=\!0;startTime=Date.now();draw()}}document.addEventListener("click",clickHandler);document.addEventListener("keydown",keyHandler);setInterval(()=\>{if(running)spawnDot()},500);draw()})();

Block game  
javascript:(()=\>{if(document.getElementById("cubeRunnerGame"))return;var canvas=document.createElement("canvas");canvas.id="cubeRunnerGame";canvas.width=400;canvas.height=400;Object.assign(canvas.style,{position:"fixed",left:"50%",top:"50%",transform:"translate(-50%,-50%)",zIndex:999999999,border:"4px solid \#333",borderRadius:"10px",background:"white"});document.body.appendChild(canvas);var ctx=canvas.getContext("2d");var player={x:50,y:350,size:20,dy:0,gravity:0.8,jumpPower:-14,isDuck:false};var obstacles=\[\],score=0,speed=4,gameOver=false,lastObstacleX=0,minDistance=20,maxDistance=30;function spawnObstacle(){if(lastObstacleX\>canvas.width-minDistance)return;var r=Math.random(),type,size=20+Math.random()\*20;if(r\<0.5)type=0;else if(r\<0.85)type=1;else type=2;if(type===0)obstacles.push({x:canvas.width,y:370-size,size:size,type:0});else if(type===1)obstacles.push({x:canvas.width,y:370-size\*2,size:size,type:1});else{var h=player.size\*1.5;var y=350-player.size/2-h;obstacles.push({x:canvas.width,y:y,size:size,height:h,type:2});}lastObstacleX=canvas.width;}function resetGame(){player.y=350;player.dy=0;player.isDuck=false;obstacles=\[\];score=0;speed=4;gameOver=false;lastObstacleX=0;minDistance=20;maxDistance=30;update();}document.addEventListener("keydown",function(e){if(\!gameOver){if((e.code==="Space"||e.code==="ArrowUp")&&\!player.isDuck&\&player.y\>=350)player.dy=player.jumpPower;if(e.code==="ArrowDown"||e.code==="ShiftLeft"||e.code==="ShiftRight")player.isDuck=true;}if(e.code==="KeyR"&\&gameOver)resetGame();if(e.code==="Escape"){canvas.remove();gameOver=true;}});document.addEventListener("keyup",function(e){if(e.code==="ArrowDown"||e.code==="ShiftLeft"||e.code==="ShiftRight")player.isDuck=false;});function update(){ctx.clearRect(0,0,canvas.width,canvas.height);ctx.fillStyle="black";ctx.fillRect(0,370,canvas.width,2);if(\!gameOver){player.dy+=player.gravity;player.y+=player.dy;if(player.y\>350)player.y=350;var dh=player.isDuck?player.size/2:player.size;ctx.fillStyle="blue";ctx.fillRect(player.x,player.y+(player.size-dh),player.size,dh);for(var i=obstacles.length-1;i\>=0;i--){var o=obstacles\[i\];o.x-=speed;ctx.fillStyle="red";if(o.type===0)ctx.fillRect(o.x,o.y,o.size,o.size);else if(o.type===1)ctx.fillRect(o.x,o.y,o.size,o.size\*2);else ctx.fillRect(o.x,o.y,o.size,o.height);var pTop=player.y+(player.size-dh),pBot=player.y+player.size;var oBot=o.type===0?o.y+o.size:o.type===1?o.y+o.size\*2:o.y+o.height;if(player.x\<o.x+o.size&\&player.x+player.size\>o.x&\&pTop\<oBot&\&pBot\>o.y)gameOver=true;if(o.x+o.size\<0){obstacles.splice(i,1);lastObstacleX=0;}}score+=0.1;ctx.fillStyle="black";ctx.font="20px Arial";ctx.fillText("Score: "+Math.floor(score),10,30);speed+=0.005;minDistance+=0.02;maxDistance+=0.02;requestAnimationFrame(update);}else{ctx.fillStyle="black";ctx.font="24px Arial";ctx.textAlign="center";ctx.fillText("GAME OVER\!",200,180);ctx.font="18px Arial";ctx.fillText("R \= Reset   ESC \= Quit",200,220);ctx.textAlign="start";}}setInterval(()=\>{if(\!gameOver)spawnObstacle();},1200);update();})();

Snake  
javascript:(()=\>{const canvas=document.createElement("canvas");const size=300,grid=10,cell=size/grid;Object.assign(canvas.style,{position:"fixed",left:"50%",top:"50%",transform:"translate(-50%,-50%)",background:"\#0e0e0e%22,border:%222px%20solid%20\#444%22,zIndex:99999});canvas.width=canvas.height=size;document.body.appendChild(canvas);const%20ctx=canvas.getContext(%222d%22);let%20snake,dir,apple,alive,loop,score=0,highScore=0;function%20resetGame(){snake=\[{x:5,y:5}\];dir={x:1,y:0};apple=spawnApple();alive=true;score=0;draw();clearInterval(loop);loop=setInterval(tick,300)}function%20cleanup(){clearInterval(loop);window.removeEventListener(%22keydown%22,keyHandler);canvas.remove()}function%20spawnApple(){let%20p;do{p={x:Math.floor(Math.random()\*grid),y:Math.floor(Math.random()\*grid)}}while(snake.some(s=%3Es.x===p.x&\&s.y===p.y));return%20p}function%20keyHandler(e){if(e.key===%22Escape%22){cleanup();return}if(e.key.toLowerCase()===%22r%22){resetGame();return}if(\!alive)return;const%20d={ArrowUp:{x:0,y:-1},ArrowDown:{x:0,y:1},ArrowLeft:{x:-1,y:0},ArrowRight:{x:1,y:0}}\[e.key\];if(\!d)return;if(snake.length%3E1&\&d.x===-dir.x&\&d.y===-dir.y)return;dir=d}window.addEventListener(%22keydown%22,keyHandler);function%20drawGrid(){ctx.strokeStyle=%22\#222%22;for(let%20i=0;i%3C=grid;i++){ctx.beginPath();ctx.moveTo(i\*cell,0);ctx.lineTo(i\*cell,size);ctx.moveTo(0,i\*cell);ctx.lineTo(size,i\*cell);ctx.stroke()}}function%20drawHUD(){ctx.fillStyle=%22\#888%22;ctx.font=%2212px%20monospace%22;ctx.textBaseline=%22top%22;ctx.textAlign=%22left%22;ctx.fillText(%60score%20${score}%60,6,6);ctx.textAlign=%22right%22;ctx.fillText(%60high%20${highScore}%60,size-6,6)}function%20draw(){ctx.fillStyle=%22\#0e0e0e%22;ctx.fillRect(0,0,size,size);drawGrid();ctx.fillStyle=%22\#6aff6a%22;snake.forEach(s=%3Ectx.fillRect(s.x\*cell+3,s.y\*cell+3,cell-6,cell-6));ctx.fillStyle=%22\#ff5555%22;ctx.fillRect(apple.x\*cell+4,apple.y\*cell+4,cell-8,cell-8);drawHUD()}function%20deathScreen(){ctx.fillStyle=%22rgba(0,0,0,0.75)%22;ctx.fillRect(0,0,size,size);ctx.fillStyle=%22\#aaa%22;ctx.font=%2220px%20monospace%22;ctx.textAlign=%22center%22;ctx.textBaseline=%22middle%22;ctx.fillText(%22GAME%20OVER%22,size/2,size/2-10);ctx.font=%2212px%20monospace%22;ctx.fillText(%22R%20%E2%80%94%20Reset%20%20%20ESC%20%E2%80%94%20Quit%22,size/2,size/2+15)}function%20tick(){if(\!alive)return;const%20head={x:snake\[0\].x+dir.x,y:snake\[0\].y+dir.y};if(head.x%3C0||head.y%3C0||head.x%3E=grid||head.y%3E=grid||snake.some(s=%3Es.x===head.x&\&s.y===head.y)){alive=false;clearInterval(loop);draw();deathScreen();return}snake.unshift(head);if(head.x===apple.x&\&head.y===apple.y){score++;if(score%3EhighScore)highScore=score;apple=spawnApple()}else%20snake.pop();draw()}resetGame()})();

Singleplayer Pong (wasd or arrow keys)  
javascript:(()=\>{if(document.getElementById("pongGame"))return;const c=document.createElement("canvas");c.id="pongGame";c.width=500;c.height=350;Object.assign(c.style,{position:"fixed",left:"50%",top:"50%",transform:"translate(-50%,-50%)",zIndex:999999999,border:"4px solid \#333",borderRadius:"10px",background:"\#fff"});document.body.appendChild(c);const x=c.getContext("2d");let player,ai,ball,score=0,high=0,over=\!1,run=\!0;function reset(){player={x:15,y:140,w:12,h:70,s:6};ai={x:c.width-27,y:140,w:12,h:70};ball={x:c.width/2,y:c.height/2,r:6,vx:Math.random()\>.5?4:-4,vy:Math.random()\*4-2};score=0;over=\!1}function clamp(){player.y\<0&&(player.y=0);player.y+player.h\>c.height&&(player.y=c.height-player.h)}function key(e){run&&(("w"===e.key||"ArrowUp"===e.key)&&(player.y-=24),("s"===e.key||"ArrowDown"===e.key)&&(player.y+=24),clamp(),"r"\!==e.key&&"R"\!==e.key||(reset(),requestAnimationFrame(loop)),"Escape"===e.key&\&quit())}function quit(){run=\!1;document.removeEventListener("keydown",key);c.remove()}function hit(p){return ball.x-ball.r\<p.x+p.w&\&ball.x+ball.r\>p.x&\&ball.y+ball.r\>p.y&\&ball.y-ball.r\<p.y+p.h}function loop(){if(\!run||over)return;x.clearRect(0,0,c.width,c.height);ai.y+=(ball.y-(ai.y+ai.h/2))\*.08;ai.y\<0&&(ai.y=0);ai.y+ai.h\>c.height&&(ai.y=c.height-ai.h);ball.x+=ball.vx;ball.y+=ball.vy;(ball.y\<ball.r||ball.y\>c.height-ball.r)&&(ball.vy\*=-1);hit(player)&&(ball.vx=Math.abs(ball.vx)+.2,ball.vy+=(ball.y-(player.y+player.h/2))\*.05,score++,high=Math.max(high,score));hit(ai)&&(ball.vx=-Math.abs(ball.vx));ball.x\<0&&(over=\!0);ball.x\>c.width&&(ball.x=c.width/2,ball.y=c.height/2,ball.vx=-4,ball.vy=Math.random()\*4-2);x.fillStyle="black";x.fillRect(player.x,player.y,player.w,player.h);x.fillRect(ai.x,ai.y,ai.w,ai.h);x.beginPath();x.arc(ball.x,ball.y,ball.r,0,2\*Math.PI);x.fill();x.font="18px sans-serif";x.fillText("Score: "+score,10,22);x.fillText("High: "+high,c.width-110,22);over?(x.fillStyle="red",x.font="28px sans-serif",x.fillText("GAME OVER",150,170),x.font="16px sans-serif",x.fillText("R \= Restart   ESC \= Quit",140,200)):requestAnimationFrame(loop)}document.addEventListener("keydown",key);reset();requestAnimationFrame(loop)})();

Two player pong (wasd and arrow keys)  
javascript:(() \=\> {if(document.getElementById("pong2P"))return;const c=document.createElement("canvas");c.id="pong2P";c.width=600;c.height=350;Object.assign(c.style,{position:"fixed",left:"50%",top:"50%",transform:"translate(-50%,-50%)",zIndex:999999999,border:"4px solid \#333",borderRadius:"10px",background:"\#fff"});document.body.appendChild(c);const x=c.getContext("2d");const paddleH=70,paddleW=12;let lp={x:15,y:140,v:0};let rp={x:c.width-27,y:140,v:0};let ball={x:300,y:175,r:6,vx:4,vy:2};let ls=0,rs=0;let running=true;const keys={};function reset(dir=1){ball.x=c.width/2;ball.y=c.height/2;ball.vx=4\*dir;ball.vy=(Math.random()\*4-2);}function clamp(p){p.y=Math.max(0,Math.min(c.height-paddleH,p.y));}function hit(p){return ball.x-ball.r\<p.x+paddleW&\&ball.x+ball.r\>p.x&\&ball.y+ball.r\>p.y&\&ball.y-ball.r\<p.y+paddleH;}function loop(){if(\!running)return;lp.v=(keys.w?-6:0)+(keys.s?6:0);rp.v=(keys.ArrowUp?-6:0)+(keys.ArrowDown?6:0);lp.y+=lp.v;rp.y+=rp.v;clamp(lp);clamp(rp);ball.x+=ball.vx;ball.y+=ball.vy;if(ball.y\<ball.r||ball.y\>c.height-ball.r)ball.vy\*=-1;if(hit(lp)){ball.vx=Math.abs(ball.vx);ball.vy+=(ball.y-(lp.y+paddleH/2))\*0.05;}if(hit(rp)){ball.vx=-Math.abs(ball.vx);ball.vy+=(ball.y-(rp.y+paddleH/2))\*0.05;}if(ball.x\<0){rs++;reset(1);}if(ball.x\>c.width){ls++;reset(-1);}x.clearRect(0,0,c.width,c.height);x.fillStyle="black";x.fillRect(lp.x,lp.y,paddleW,paddleH);x.fillRect(rp.x,rp.y,paddleW,paddleH);x.beginPath();x.arc(ball.x,ball.y,ball.r,0,Math.PI\*2);x.fill();x.font="18px sans-serif";x.fillText(ls,c.width/2-40,25);x.fillText(rs,c.width/2+25,25);requestAnimationFrame(loop);}function key(e){keys\[e.key\]=e.type==="keydown";if(e.key==="Escape")quit();}function quit(){running=false;document.removeEventListener("keydown",key);document.removeEventListener("keyup",key);c.remove();}document.addEventListener("keydown",key);document.addEventListener("keyup",key);reset(Math.random()\>0.5?1:-1);requestAnimationFrame(loop);})();

Platform Jump  
javascript:(()=\>{if(document.getElementById("platformGame"))return;const c=document.createElement("canvas");c.id="platformGame";c.width=400;c.height=500;Object.assign(c.style,{position:"fixed",left:"50%",top:"50%",transform:"translate(-50%,-50%)",zIndex:999999999,border:"4px solid \#333",borderRadius:"10px",background:"\#fff"});document.body.appendChild(c);const x=c.getContext("2d");const keys={};let player,plats,stars;let score=0,high=0;let running=true,gameOver=false;const gravity=0.4,fallSpeed=1.4,platH=8;function reset(){player={x:c.width/2,y:c.height/2-40,r:10,vx:0,vy:0,onGround:false};plats=\[\];stars=\[\];score=0;gameOver=false;const startW=80,startX=c.width/2-startW/2,startY=c.height/2;plats.push({x:startX,y:startY,w:startW,h:platH});const spacing=40\*1.5;for(let i=1;i\<9;i++)spawnPlatform(startY-i\*spacing);}function spawnPlatform(y=-platH){const minW=platH,w=Math.random()\*60+minW+30,px=Math.random()\*(c.width-w),p={x:px,y,w,h:platH};plats.push(p);if(Math.random()\<0.45)stars.push({s:12,on:p});}function key(e){keys\[e.key\]=e.type==="keydown";if(gameOver&&(e.key==="r"||e.key==="R"))reset();if(e.key==="Escape")quit();}function quit(){running=false;document.removeEventListener("keydown",key);document.removeEventListener("keyup",key);c.remove();}function loop(){if(\!running)return;if(\!gameOver){player.vx=(keys.a||keys.ArrowLeft?-4:0)+(keys.d||keys.ArrowRight?4:0);if((keys.w||keys.ArrowUp||keys\[" "\])&\&player.onGround){player.vy=-9;player.onGround=false;}player.vy+=gravity;player.x+=player.vx;player.y+=player.vy;if(player.x\<0)player.x=0;if(player.x\>c.width)player.x=c.width;player.onGround=false;for(let i=plats.length-1;i\>=0;i--){const p=plats\[i\];p.y+=fallSpeed;if(player.vy\>0&\&player.y+player.r\>p.y&\&player.y+player.r\<p.y+p.h&\&player.x\>p.x&\&player.x\<p.x+p.w){player.y=p.y-player.r;player.vy=0;player.onGround=true;}if(p.y\>c.height){stars=stars.filter(s=\>s.on\!==p);plats.splice(i,1);spawnPlatform();}}for(let i=stars.length-1;i\>=0;i--){const s=stars\[i\];const p=s.on;const sx=p.x+p.w/2-s.s/2,sy=p.y-14;if(Math.abs(player.x-(sx+s.s/2))\<player.r+s.s/2&\&Math.abs(player.y-(sy+s.s/2))\<player.r+s.s/2){score++;high=Math.max(high,score);stars.splice(i,1);}}if(player.y-player.r\>c.height)gameOver=true;}x.clearRect(0,0,c.width,c.height);x.fillStyle="black";plats.forEach(p=\>x.fillRect(p.x,p.y,p.w,p.h));x.fillStyle="gold";stars.forEach(s=\>{const p=s.on;x.fillRect(p.x+p.w/2-s.s/2,p.y-14,s.s,s.s);});x.fillStyle="dodgerblue";x.beginPath();x.arc(player.x,player.y,player.r,0,Math.PI\*2);x.fill();x.fillStyle="black";x.font="18px sans-serif";x.fillText("Score: "+score,10,22);x.fillText("High: "+high,c.width-110,22);if(gameOver){x.fillStyle="red";x.font="30px sans-serif";x.fillText("GAME OVER",105,240);x.font="16px sans-serif";x.fillText("R \= Restart   ESC \= Quit",95,270);}requestAnimationFrame(loop);}document.addEventListener("keydown",key);document.addEventListener("keyup",key);reset();requestAnimationFrame(loop);})();

Mini Shooter  
javascript:(()=\>{if(document.getElementById("shooterGame"))return;const c=document.createElement("canvas");c.id="shooterGame";c.width=500;c.height=500;Object.assign(c.style,{position:"fixed",left:"50%",top:"50%",transform:"translate(-50%,-50%)",zIndex:999999999,border:"4px solid \#333",borderRadius:"10px",background:"\#fff"});document.body.appendChild(c);const x=c.getContext("2d");let keys={},player,playerShots=\[\],enemyShots=\[\],enemies=\[\],score=0,high=0,lives=3,gameOver=false,run=true,lastEnemyShot=0,lastPlayerShot=0,hitAnimation=null;const lifeColors=\["dodgerblue","limegreen","purple"\];function reset(){player={x:c.width/2,y:c.height-40,r:12,color:lifeColors\[0\]};playerShots=\[\];enemyShots=\[\];enemies=\[\];score=0;lives=3;gameOver=false;hitAnimation=null;spawnWave()}function spawnWave(){enemies=\[\];for(let i=0;i\<5;i++){enemies.push({x:50+i\*80,y:50,w:35,h:5})}}function key(e){keys\[e.key\]=e.type==="keydown";if(gameOver&&(e.key==="r"||e.key==="R"))reset();if(e.key==="Escape")quit()}function quit(){run=false;document.removeEventListener("keydown",key);document.removeEventListener("keyup",key);c.remove()}function shootPlayer(){playerShots.push({x:player.x-2.5,y:player.y-player.r-10,w:5,h:10,vy:-6})}function shootEnemies(){enemies.forEach(e=\>{enemyShots.push({x:e.x+e.w/2-2.5,y:e.y+e.h,w:5,h:10,vy:4})})}function triggerHitAnimation(){hitAnimation={startTime:Date.now(),duration:1500,radius:0}}function loop(){if(\!run)return;const now=Date.now();const freeze=hitAnimation&\&now-hitAnimation.startTime\<hitAnimation.duration;if(\!gameOver&&\!freeze){if(keys.a||keys.ArrowLeft)player.x-=5;if(keys.d||keys.ArrowRight)player.x+=5;if(keys.w||keys.ArrowUp)player.y-=5;if(keys.s||keys.ArrowDown)player.y+=5;player.x=Math.max(0,Math.min(c.width,player.x));player.y=Math.max(0,Math.min(c.height,player.y));if(now-lastPlayerShot\>500){shootPlayer();lastPlayerShot=now}if(now-lastEnemyShot\>1000){shootEnemies();lastEnemyShot=now}playerShots.forEach((s,i)=\>{s.y+=s.vy;enemies.forEach((e,j)=\>{if(s.x\<e.x+e.w&\&s.x+s.w\>e.x&\&s.y\<e.y+e.h&\&s.y+s.h\>e.y){score++;high=Math.max(high,score);enemies.splice(j,1);playerShots.splice(i,1)}});if(s.y\<0)playerShots.splice(i,1)});enemyShots.forEach((s,i)=\>{s.y+=s.vy;if(s.x\<player.x+player.r&\&s.x+s.w\>player.x-player.r&\&s.y\<player.y+player.r&\&s.y+s.h\>player.y-player.r){lives--;triggerHitAnimation();enemyShots.splice(i,1);if(lives\>0){player.color=lifeColors\[3-lives\]}else{gameOver=true}}});if(enemies.length===0)spawnWave()}x.clearRect(0,0,c.width,c.height);if(\!freeze){x.fillStyle=player.color;x.beginPath();x.arc(player.x,player.y,player.r,0,2\*Math.PI);x.fill();x.fillStyle="green";enemies.forEach(e=\>x.fillRect(e.x,e.y,e.w,e.h));x.fillStyle="red";playerShots.forEach(s=\>x.fillRect(s.x,s.y,s.w,s.h));enemyShots.forEach(s=\>x.fillRect(s.x,s.y,s.w,s.h))}x.fillStyle="black";x.font="18px sans-serif";x.fillText("Score: "+score,10,22);x.fillText("High: "+high,c.width-110,22);for(let i=0;i\<lives;i++){x.fillStyle=lifeColors\[i\];x.beginPath();x.arc(c.width-20-30\*i,c.height-20,10,0,2\*Math.PI);x.fill()}if(hitAnimation){const elapsed=now-hitAnimation.startTime;if(elapsed\<hitAnimation.duration){const progress=elapsed/hitAnimation.duration;const radius=progress\*100;x.fillStyle="orange";x.beginPath();x.arc(player.x,player.y,radius,0,2\*Math.PI);x.fill()}else{hitAnimation=null}}if(gameOver){x.fillStyle="red";x.font="30px sans-serif";x.fillText("GAME OVER",130,220);x.font="16px sans-serif";x.fillText("R \= Reset   ESC \= Quit",130,250)}requestAnimationFrame(loop)}document.addEventListener("keydown",key);document.addEventListener("keyup",key);reset();requestAnimationFrame(loop);})();

Breakout  
javascript:(()=\>{if(document.getElementById("breakoutGame"))return;const c=document.createElement("canvas");c.id="breakoutGame";c.width=500;c.height=400;Object.assign(c.style,{position:"fixed",left:"50%",top:"50%",transform:"translate(-50%,-50%)",zIndex:999999999,border:"4px solid \#333%22,background:%22\#fff%22});document.body.appendChild(c);const%20x=c.getContext(%222d%22);let%20paddle,ball,blocks=\[\],particles=\[\];let%20score=0,high=0,level=1,lives=3;let%20gameOver=false,running=true;let%20keys={},useMouse=false;const%20themes=\[%22\#8ecae6%22,%22red%22,%22orange%22,%22yellow%22,%22green%22,%22\#023047%22,%22purple%22,%22black%22\];document.addEventListener(%22mousemove%22,e=%3E{const%20r=c.getBoundingClientRect();useMouse=e.clientX%3E=r.left&\&e.clientX%3C=r.right&\&e.clientY%3E=r.top&\&e.clientY%3C=r.bottom;if(useMouse)paddle.x=e.clientX-r.left-paddle.w/2});document.addEventListener(%22keydown%22,e=%3E{keys\[e.key\]=true;if(gameOver&&(e.key===%22r%22||e.key===%22R%22))reset();if(e.key===%22Escape%22)quit()});document.addEventListener(%22keyup%22,e=%3Ekeys\[e.key\]=false);function%20quit(){running=false;c.remove()}function%20reset(){paddle={x:c.width/2-12.5,y:c.height-25,w:25,h:5,color:%22green%22};ball={x:c.width/2,y:paddle.y-10,r:3.5,vx:(Math.random()-.5),vy:-2};score=0;lives=3;level=1;gameOver=false;particles=\[\];spawnBlocks()}function%20spawnBlocks(){blocks=\[\];const%20w=13,h=5,cols=20,rows=5,sp=w,total=cols\*w+(cols-1)\*sp,startX=(c.width-total)/2,startY=40;for(let%20r=0;r%3Crows;r++)for(let%20i=0;i%3Ccols;i++)blocks.push({x:startX+i\*(w+sp),y:startY+r\*(h+sp),w,h})}function%20spawnParticles(){particles=\[\];for(let%20i=0;i%3C10;i++)particles.push({x:paddle.x+paddle.w/2,y:paddle.y,w:5,h:10,vx:Math.random()\*4-2,vy:Math.random()\*-4-1,life:60})}function%20loop(){if(\!running)return;const%20theme=themes\[(level-1)%themes.length\];if(\!gameOver){if(\!useMouse){if(keys.a||keys.ArrowLeft)paddle.x-=4;if(keys.d||keys.ArrowRight)paddle.x+=4}paddle.x=Math.max(0,Math.min(c.width-paddle.w,paddle.x));ball.x+=[ball.vx](http://ball.vx);ball.y+=ball.vy;if(ball.x%3Cball.r||ball.x%3Ec.width-ball.r)ball.vx\*=-1;if(ball.y%3Cball.r)ball.vy\*=-1;if(ball.x%3Epaddle.x&\&ball.x%3Cpaddle.x+paddle.w&\&ball.y+ball.r%3Epaddle.y&\&ball.y%3Cpaddle.y+paddle.h){let%20hit=(ball.x-(paddle.x+paddle.w/2))/(paddle.w/2);hit+=(Math.random()-.5)\*.2;const%20s=2;ball.vx=hit\*s;ball.vy=-Math.abs(s);ball.y=paddle.y-ball.r}blocks.forEach((b,i)=%3E{if(ball.x%3Eb.x&\&ball.x%3Cb.x+b.w&\&ball.y%3Eb.y&\&ball.y%3Cb.y+b.h){blocks.splice(i,1);score++;high=Math.max(high,score);ball.vx+=(Math.random()-.5)\*.6;ball.vy\*=-1}});if(ball.y%3Ec.height){lives--;spawnParticles();paddle.color=\[%22green%22,%22lime%22,%22cyan%22\]\[lives\]||%22gray%22;if(lives%3C=0)gameOver=true;else{ball.x=c.width/2;ball.y=paddle.y-10;ball.vx=Math.random()-.5;ball.vy=-2}}if(blocks.length===0){level++;spawnBlocks()}}x.clearRect(0,0,c.width,c.height);x.fillStyle=theme;blocks.forEach(b=%3Ex.fillRect(b.x,b.y,b.w,b.h));x.fillStyle=paddle.color;x.fillRect(paddle.x,paddle.y,paddle.w,paddle.h);x.beginPath();x.arc(ball.x,ball.y,ball.r,0,Math.PI\*2);x.fill();x.fillStyle=%22orange%22;particles.forEach(p=%3E{p.x+=p.vx;p.y+=p.vy;p.vy+=.2;p.life--;x.fillRect(p.x,p.y,p.w,p.h)});particles=particles.filter(p=%3Ep.life%3E0);x.fillStyle=%22black%22;x.font=%2214px%20sans-serif%22;x.fillText(%22Score:%20%22+score,10,18);x.fillText(%22Level:%20%22+level,c.width/2-25,18);x.fillText(%22High:%20%22+high,c.width-90,18);for(let%20i=0;iew %3Clives;i++){x.fillStyle=\[%22green%22,%22lime%22,%22cyan%22\]\[i\];x.fillRect(c.width-30-i\*30,c.height-15,25,5)}if(gameOver){x.fillStylesw\`sw=%22red%22;x.font=%2226px%20sans-serif%22;x.fillText(%22GAME%20OVER%22,150,200);x.font=%2214px%20sans-serif%22;x.fillText(%22R%20=%20Reset%20%20%20ES5C%20=%20Quit%22,155,225)}requestAnimationFrame(loop)}reset();loop()})();

Physics Demonstration  
javascript:(()=\>{if(document.getElementById("powderCircle"))return;const B=3,R=60,D=R\*2,U=50,W=D,H=D,A=0,S=1,WTR=2,SD=3,M=\[{id:S,n:"Block",c:"\#000"},{id:WTR,n:"Water",c:"\#1e90ff"},{id:SD,n:"Sand",c:"\#d2b48c"}\];let sel=S,md=\!1,erase=\!1,bs=1,MIN=1,MAX=8;const c=document.createElement("canvas");c.id="powderCircle";c.width=W\*B;c.height=H\*B+U;Object.assign(c.style,{position:"fixed",left:"50%",top:"50%",transform:"translate(-50%,-50%)",background:"\#fff",border:"2px solid \#aaa",zIndex:999999,cursor:"crosshair"});document.body.appendChild(c);const x=c.getContext("2d"),g=Array.from({length:H},()=\>Array(W).fill(A)),cx=R,cy=R,inside=(x,y)=\>{const dx=x-cx,dy=y-cy;return dx\*dx+dy\*dy\<=R\*R};const step=()=\>{for(let y=H-2;y\>=0;y--)for(let x0=0;x0\<W;x0++){if(\!inside(x0,y))continue;const v=g\[y\]\[x0\];if(v===SD){const ny=y+1;if(inside(x0,ny)){const b=g\[ny\]\[x0\];if(b===A||b===WTR){g\[ny\]\[x0\]=SD;g\[y\]\[x0\]=b}}}if(v===WTR){const ny=y+1;if(inside(x0,ny)&\&g\[ny\]\[x0\]===A){g\[ny\]\[x0\]=WTR;g\[y\]\[x0\]=A}else{const d=Math.random()\<.5?\[-1,1\]:\[1,-1\];for(const dx of d){const nx=x0+dx;if(inside(nx,y)&\&g\[y\]\[nx\]===A){g\[y\]\[nx\]=WTR;g\[y\]\[x0\]=A;break}}}}}};const t=setInterval(step,250);const draw=()=\>{x.clearRect(0,0,c.width,c.height);for(let y=0;y\<H;y++)for(let x0=0;x0\<W;x0++){if(\!inside(x0,y))continue;const v=g\[y\]\[x0\];if(v\!==A){x.fillStyle=M.find(m=\>m.id===v).c;x.fillRect(x0\*B,y\*B,B,B)}}x.strokeStyle="\#999";x.beginPath();x.arc(cx\*B,cy\*B,R\*B,0,Math.PI\*2);x.stroke();x.fillStyle="\#f0f0f0";x.fillRect(0,H\*B,c.width,U);M.forEach((m,i)=\>{const px=15+i\*90,py=H\*B+10;x.fillStyle=m.c;x.fillRect(px,py,24,24);x.fillStyle="\#000";x.font="13px sans-serif";x.fillText(m.n,px+32,py+17);if(sel===m.id)x.strokeRect(px-2,py-2,28,28)});x.font="12px monospace";x.fillText("Brush:"+bs,c.width-90,H\*B+30);requestAnimationFrame(draw)};draw();const paint=(mx,my)=\>{const gx=Math.floor(mx/B),gy=Math.floor(my/B);for(let dy=-bs;dy\<=bs;dy++)for(let dx=-bs;dx\<=bs;dx++){if(dx\*dx+dy\*dy\>bs\*bs)continue;const x0=gx+dx,y0=gy+dy;if(x0\<0||y0\<0||x0\>=W||y0\>=H||\!inside(x0,y0))continue;g\[y0\]\[x0\]=erase?A:sel}};c.addEventListener("mousedown",e=\>{const r=c.getBoundingClientRect(),mx=e.clientX-r.left,my=e.clientY-r.top;md=\!0;erase=e.button===2;if(my\>H\*B){M.forEach((m,i)=\>{const px=15+i\*90,py=H\*B+10;if(mx\>=px&\&mx\<=px+24&\&my\>=py&\&my\<=py+24)sel=m.id});return}paint(mx,my)});c.addEventListener("mousemove",e=\>{if(\!md)return;const r=c.getBoundingClientRect();paint(e.clientX-r.left,e.clientY-r.top)});window.addEventListener("mouseup",()=\>md=\!1);c.addEventListener("contextmenu",e=\>e.preventDefault());document.addEventListener("keydown",e=\>{if(e.key==="=")bs=Math.min(MAX,bs+1);if(e.key==="-" )bs=Math.max(MIN,bs-1);if(e.key==="Escape"){clearInterval(t);c.remove()}if(e.key.toLowerCase()==="r")for(let y=0;y\<H;y++)for(let x0=0;x0\<W;x0++)g\[y\]\[x0\]=A})})();

Fruit Ninja  
javascript:(()=\>{if(document.getElementById("dodgeGame"))return;const SCALE=1.3,ORIGINAL\_W=400,ORIGINAL\_H=400,c=document.createElement("canvas");c.id="dodgeGame";c.width=ORIGINAL\_W\*SCALE;c.height=ORIGINAL\_H\*SCALE;Object.assign(c.style,{position:"fixed",left:"50%",top:"50%",transform:"translate(-50%,-50%)",zIndex:999999999,border:"4px solid \#333",borderRadius:"10px",background:"\#fff"});document.body.appendChild(c);const x=c.getContext("2d");const WALL\_PADDING=6,WALL\_BOUNCE=.9;let fruits=\[\],halves=\[\],slashes=\[\],score=0,highScore=0,lives=3,paused=false;const COLORS=\["\#FFD700","\#FF4D4D","\#9B59B6","\#3498DB","\#8B4513"\];function resetGame(){fruits=\[\];halves=\[\];slashes=\[\];score=0;lives=3;paused=false}let mouse={x:0,y:0,px:0,py:0};c.addEventListener("mousemove",e=\>{const r=c.getBoundingClientRect();mouse.px=mouse.x;mouse.py=mouse.y;mouse.x=e.clientX-r.left;mouse.y=e.clientY-r.top;slashes.push({x1:mouse.px,y1:mouse.py,x2:mouse.x,y2:mouse.y,life:12})});window.addEventListener("keydown",e=\>{if(e.key==="Escape")c.remove();if(e.key.toLowerCase()==="p")paused=\!paused;if(e.key.toLowerCase()==="r")resetGame()});function spawnFruit(){fruits.push({x:Math.random()\*c.width,y:c.height+40,vx:(Math.random()-.5)\*3,vy:-12-Math.random()\*6,r:32,color:COLORS\[Math.floor(Math.random()\*COLORS.length)\],sliced:false})}const MIN\_SPAWN=800,MAX\_SPAWN=1200;function scheduleNextSpawn(){setTimeout(()=\>{spawnFruit();scheduleNextSpawn()},Math.random()\*(MAX\_SPAWN-MIN\_SPAWN)+MIN\_SPAWN)}scheduleNextSpawn();function distToLine(px,py,x1,y1,x2,y2){const A=px-x1,B=py-y1,C=x2-x1,D=y2-y1,d=A\*C+B\*D,l=C\*C+D\*D;let t=d/l;t=Math.max(0,Math.min(1,t));const dx=x1+t\*C-px,dy=y1+t\*D-py;return Math.sqrt(dx\*dx+dy\*dy)}function drawHeart(px,py,s=4){x.fillStyle="\#e74c3c";\[\[1,0,0,1\],\[1,1,1,1\],\[1,1,1,1\]\].forEach((r,y)=\>r.forEach((b,xp)=\>{if(b)x.fillRect(px+xp\*s,py+y\*s,s,s)}))}function loop(){if(paused){x.fillStyle="rgba(255,255,255,.7)";x.fillRect(0,0,c.width,c.height);x.fillStyle="\#000";x.font="30px sans-serif";x.fillText("PAUSED",c.width/2-60,c.height/2);requestAnimationFrame(loop);return}x.clearRect(0,0,c.width,c.height);x.fillStyle="\#fff";x.fillRect(0,0,c.width,c.height);fruits.forEach(f=\>{f.x+=f.vx;f.y+=f.vy;f.vy+=.35;if(f.x-f.r\<WALL\_PADDING){f.x=f.r+WALL\_PADDING;f.vx=Math.abs(f.vx)\*WALL\_BOUNCE}if(f.x+f.r\>c.width-WALL\_PADDING){f.x=c.width-f.r-WALL\_PADDING;f.vx=-Math.abs(f.vx)\*WALL\_BOUNCE}x.beginPath();x.arc(f.x,f.y,f.r,0,Math.PI\*2);x.fillStyle=f.color;x.fill();slashes.forEach(s=\>{if(\!f.sliced&\&distToLine(f.x,f.y,s.x1,s.y1,s.x2,s.y2)\<f.r){f.sliced=true;score+=10;halves.push({x:f.x,y:f.y,vx:-3,vy:-3,r:f.r/1.4},{x:f.x,y:f.y,vx:3,vy:-3,r:f.r/1.4})}})});fruits.forEach(f=\>{if(\!f.sliced&\&f.y\>c.height+60){lives--;f.sliced=true}});fruits=fruits.filter(f=\>\!f.sliced);halves.forEach(h=\>{h.x+=h.vx;h.y+=h.vy;h.vy+=.4;x.beginPath();x.arc(h.x,h.y,h.r,0,Math.PI\*2);x.fillStyle="\#2ecc71";x.fill()});halves=halves.filter(h=\>h.y\<c.height+60);slashes.forEach(s=\>{x.strokeStyle=\`rgba(0,0,0,${s.life/12})\`;x.lineWidth=7;x.beginPath();x.moveTo(s.x1,s.y1);x.lineTo(s.x2,s.y2);x.stroke();s.life--});slashes=slashes.filter(s=\>s.life\>0);highScore=Math.max(highScore,score);x.fillStyle="\#000";x.font="18px sans-serif";x.fillText("Score: "+score,10,25);x.fillText("High: "+highScore,c.width-120,25);x.fillText("\[P\] Pause  \[R\] Restart",10,c.height-10);for(let i=0;i\<lives;i++)drawHeart(c.width-20-i\*20,c.height-20,4);if(lives\<=0){x.fillStyle="rgba(255,255,255,.85)";x.fillRect(0,0,c.width,c.height);x.fillStyle="\#000";x.font="28px sans-serif";x.fillText("GAME OVER",c.width/2-90,c.height/2);x.font="18px sans-serif";x.fillText("Press R to restart or ESC to quit",c.width/2-150,c.height/2+30);requestAnimationFrame(loop);return}requestAnimationFrame(loop)}loop()})();

javascript:(function(){if(document.getElementById('floating-chat-container')){document.getElementById('floating-chat-container').remove();document.getElementById('floating-chat-button')?.remove();document.body.style.overflow='';return;}let HEADER\_HEIGHT=46;let container=document.createElement('div');container.id='floating-chat-container';container.style.cssText='position:fixed;inset:0;width:100vw;height:100vh;z-index:100000;overflow:hidden;font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;background:\#111;';let header=document.createElement('div');header.style.cssText='background:\#333;color:white;padding:10px 14px;display:flex;justify-content:space-between;align-items:center;user-select:none;position:absolute;top:0;left:0;right:0;height:'+HEADER\_HEIGHT+'px;box-sizing:border-box;z-index:100001;';let title=document.createElement('span');title.textContent='Chat (Fullscreen)';header.appendChild(title);let buttons=document.createElement('div');buttons.style.cssText='display:flex;gap:10px;';let minBtn=document.createElement('button');minBtn.innerHTML='−';minBtn.style.cssText='background:none;border:none;color:white;font-size:22px;cursor:pointer;';let closeBtn=document.createElement('button');closeBtn.innerHTML='✕';closeBtn.style.cssText='background:none;border:none;color:white;font-size:20px;cursor:pointer;';buttons.appendChild(minBtn);buttons.appendChild(closeBtn);header.appendChild(buttons);let iframe=document.createElement('iframe');iframe.src='https://chat-s0cb.onrender.com/';iframe.style.cssText='position:absolute;top:'+HEADER\_HEIGHT+'px;left:0;width:100%;height:calc(100% \- '+HEADER\_HEIGHT+'px);border:none;';container.appendChild(header);container.appendChild(iframe);document.body.appendChild(container);document.body.style.overflow='hidden';function createButton(){let btn=document.createElement('button');btn.id='floating-chat-button';btn.innerHTML='💬';btn.style.cssText='position:fixed;bottom:20px;right:20px;width:50px;height:50px;border-radius:50%;background:\#333;color:white;border:none;font-size:24px;cursor:pointer;z-index:100000;box-shadow:0 4px 12px rgba(0,0,0,0.15);';btn.onclick=()=\>{btn.remove();container.style.display='block';document.body.style.overflow='hidden';};document.body.appendChild(btn);}minBtn.onclick=()=\>{container.style.display='none';createButton();document.body.style.overflow='';};closeBtn.onclick=()=\>{container.remove();document.getElementById('floating-chat-button')?.remove();document.body.style.overflow='';};})();

javascript:(function(){if(document.getElementById('floating-chat-container')){document.getElementById('floating-chat-container').remove();document.getElementById('floating-chat-button')?.remove();document.body.style.overflow=%27%27;return;}let container=document.createElement(%27div%27);container.id=%27floating-chat-container%27;container.style.cssText=%27position:fixed;inset:0;width:100vw;height:100vh;z-index:100000;overflow:hidden;font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;background:\#111;';let header=document.createElement('div');header.style.cssText='background:\#333;color:white;padding:10px 14px;display:flex;justify-content:space-between;align-items:center;user-select:none;position:absolute;top:0;left:0;right:0;z-index:100001;';let title=document.createElement('span');title.textContent='Chat (Fullscreen)';header.appendChild(title);let buttons=document.createElement('div');buttons.style.cssText='display:flex;gap:10px;';let minBtn=document.createElement('button');minBtn.innerHTML='−';minBtn.style.cssText='background:none;border:none;color:white;font-size:22px;cursor:pointer;';let closeBtn=document.createElement('button');closeBtn.innerHTML='✕';closeBtn.style.cssText='background:none;border:none;color:white;font-size:20px;cursor:pointer;';buttons.appendChild(minBtn);buttons.appendChild(closeBtn);header.appendChild(buttons);let iframe=document.createElement('iframe');iframe.src='https://chat-s0cb.onrender.com/';iframe.style.cssText='width:100%;height:100%;border:none;position:absolute;top:0;left:0;';container.appendChild(header);container.appendChild(iframe);document.body.appendChild(container);document.body.style.overflow='hidden';function createButton(){let btn=document.createElement('button');btn.id='floating-chat-button';btn.innerHTML='💬';btn.style.cssText='position:fixed;bottom:20px;right:20px;width:50px;height:50px;border-radius:50%;background:\#333;color:white;border:none;font-size:24px;cursor:pointer;z-index:100000;box-shadow:0 4px 12px rgba(0,0,0,0.15);';btn.onclick=()=\>{btn.remove();container.style.display='block';document.body.style.overflow='hidden';};document.body.appendChild(btn);}minBtn.onclick=()=\>{container.style.display='none';createButton();document.body.style.overflow='';};closeBtn.onclick=()=\>{container.remove();document.getElementById('floating-chat-button')?.remove();document.body.style.overflow='';};})();

# 🎮 Finn's Games

**Disclosure: All of the games listed below were made partially with the use of Large Language Models such as ChatGPT or Copilot.**

**Available games:**  
**Mini Shooter (Finn’s Version)**

# 💬 Chat things

Things to change: offline messages receiving, switch to IRC (maybe), put messages in SUPABASE (free database)

To link text, use \<a\> href=”[https://](https://url)example.com”\>display text\</a\>

To go to the chat site, please go to [https://chat-s0cb.onrender.com](https://chat-s0cb.onrender.com) to view all of the chat, games and more.

Other fun things you can do with \<\> include

- \<mark\> to highlight your text  
- \<h1\> through \<h6\> to change your text size  
- \<progress value="50" max="100"\> to make a meter with your assigned value  
- \<marquee\> your text here \</marquee\> to make your text scroll back and forth

The commands currently added include:   
/roll (rolls a random number. Used for testing)  
 /color \#hexcodeofyourchoice (changes the color you display as)  
 /help (gives a list of all active commands. Use this more than this document, because this document might be out of date.)   
/clear (clears chat history that may be causing lag)

Cameron’s bookmarklet that un-restricts the site (may be a bit broken):  
Non-fullscreen:

```html
javascript:(function(){const storageKey='floating-chat-state';if(document.getElementById('floating-chat-iframe')){document.getElementById('floating-chat-container').remove();return;}const container=document.createElement('div');container.id='floating-chat-container';container.style.cssText='position:fixed;bottom:20px;right:20px;width:500px;height:600px;z-index:10000;border-radius:8px;box-shadow:0 4px 12px rgba(0,0,0,0.15);overflow:hidden;font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif';const header=document.createElement('div');header.style.cssText='background:#333;color:white;padding:12px 16px;display:flex;justify-content:space-between;align-items:center;cursor:grab;user-select:none';const title=document.createElement('span');title.textContent='Chat';header.appendChild(title);const buttonGroup=document.createElement('div');buttonGroup.style.cssText='display:flex;gap:8px';const minimizeBtn=document.createElement('button');minimizeBtn.innerHTML='−';minimizeBtn.style.cssText='background:none;border:none;color:white;font-size:24px;cursor:pointer;padding:0;width:30px;height:30px;display:flex;align-items:center;justify-content:center';minimizeBtn.onmouseover=()=>minimizeBtn.style.opacity='0.7';minimizeBtn.onmouseout=()=>minimizeBtn.style.opacity='1';minimizeBtn.onclick=()=>{container.style.display='none';createMinButton()};buttonGroup.appendChild(minimizeBtn);const closeBtn=document.createElement('button');closeBtn.innerHTML='✕';closeBtn.style.cssText='background:none;border:none;color:white;font-size:24px;cursor:pointer;padding:0;width:30px;height:30px;display:flex;align-items:center;justify-content:center';closeBtn.onmouseover=()=>closeBtn.style.opacity='0.7';closeBtn.onmouseout=()=>closeBtn.style.opacity='1';closeBtn.onclick=()=>{container.remove();const btn=document.getElementById('floating-chat-button');if(btn)btn.remove()};buttonGroup.appendChild(closeBtn);header.appendChild(buttonGroup);const iframe=document.createElement('iframe');iframe.id='floating-chat-iframe';iframe.src='https://chat-s0cb.onrender.com/';iframe.style.cssText='width:100%;height:calc(100% - 46px);border:none';container.appendChild(header);container.appendChild(iframe);document.body.appendChild(container);const resizeHandle=document.createElement('div');resizeHandle.style.cssText='position:absolute;bottom:0;right:0;width:20px;height:20px;background:linear-gradient(135deg,transparent 50%,#999 50%);cursor:nwse-resize;z-index:10001';container.appendChild(resizeHandle);let isDragging=false,isResizing=false,currentX,currentY,initialX,initialY,initialWidth,initialHeight;header.onmousedown=(e)=>{if(e.target.tagName==='BUTTON')return;isDragging=true;initialX=e.clientX-container.offsetLeft;initialY=e.clientY-container.offsetTop;header.style.cursor='grabbing'};resizeHandle.onmousedown=(e)=>{e.preventDefault();isResizing=true;initialX=e.clientX;initialY=e.clientY;initialWidth=container.offsetWidth;initialHeight=container.offsetHeight;resizeHandle.style.cursor='nwse-resize'};document.onmousemove=(e)=>{if(isDragging){currentX=e.clientX-initialX;currentY=e.clientY-initialY;container.style.right='auto';container.style.bottom='auto';container.style.left=currentX+'px';container.style.top=currentY+'px'}if(isResizing){const newWidth=initialWidth+(e.clientX-initialX);const newHeight=initialHeight+(e.clientY-initialY);if(newWidth>300)container.style.width=newWidth+'px';if(newHeight>200)container.style.height=newHeight+'px'}};document.onmouseup=()=>{isDragging=false;isResizing=false;header.style.cursor='grab'};function createMinButton(){const btn=document.createElement('button');btn.id='floating-chat-button';btn.innerHTML='💬';btn.style.cssText='position:fixed;bottom:20px;right:20px;width:50px;height:50px;border-radius:50%;background:#333;color:white;border:none;font-size:24px;cursor:pointer;z-index:10000;box-shadow:0 4px 12px rgba(0,0,0,0.15)';btn.onmouseover=()=>btn.style.background='#555';btn.onmouseout=()=>btn.style.background='#333';btn.onclick=()=>{btn.remove();container.style.display='block'};document.body.appendChild(btn)}})();

```

Fullscreen:

```html
javascript:(function(){if(document.getElementById('floating-chat-container')){document.getElementById('floating-chat-container').remove();document.getElementById('floating-chat-button')?.remove();document.body.style.overflow=%27%27;return;}let container=document.createElement(%27div%27);container.id=%27floating-chat-container%27;container.style.cssText=%27position:fixed;inset:0;width:100vw;height:100vh;z-index:100000;overflow:hidden;font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;background:#111;';let header=document.createElement('div');header.style.cssText='background:#333;color:white;padding:10px 14px;display:flex;justify-content:space-between;align-items:center;user-select:none;position:absolute;top:0;left:0;right:0;z-index:100001;';let title=document.createElement('span');title.textContent='Chat (Fullscreen)';header.appendChild(title);let buttons=document.createElement('div');buttons.style.cssText='display:flex;gap:10px;';let minBtn=document.createElement('button');minBtn.innerHTML='−';minBtn.style.cssText='background:none;border:none;color:white;font-size:22px;cursor:pointer;';let closeBtn=document.createElement('button');closeBtn.innerHTML='✕';closeBtn.style.cssText='background:none;border:none;color:white;font-size:20px;cursor:pointer;';buttons.appendChild(minBtn);buttons.appendChild(closeBtn);header.appendChild(buttons);let iframe=document.createElement('iframe');iframe.src='https://chat-s0cb.onrender.com/';iframe.style.cssText='width:100%;height:100%;border:none;position:absolute;top:0;left:0;';container.appendChild(header);container.appendChild(iframe);document.body.appendChild(container);document.body.style.overflow='hidden';function createButton(){let btn=document.createElement('button');btn.id='floating-chat-button';btn.innerHTML='💬';btn.style.cssText='position:fixed;bottom:20px;right:20px;width:50px;height:50px;border-radius:50%;background:#333;color:white;border:none;font-size:24px;cursor:pointer;z-index:100000;box-shadow:0 4px 12px rgba(0,0,0,0.15);';btn.onclick=()=>{btn.remove();container.style.display='block';document.body.style.overflow='hidden';};document.body.appendChild(btn);}minBtn.onclick=()=>{container.style.display='none';createButton();document.body.style.overflow='';};closeBtn.onclick=()=>{container.remove();document.getElementById('floating-chat-button')?.remove();document.body.style.overflow='';};})();
```

To make the text move in a different and more customizable way, use CSS animation injection:

```html
 <div style="
  display:inline-block;
  position:relative;
  animation: slide 2s infinite alternate;
">
  moving text
</div>

<style>
@keyframes slide {
  from { left: 0px; }
  to { left: 20px; }
}
</style>
```

Rainbows\! I have 2 different versions of a rainbow. One is animated and the other is not.   
Unanimated rainbow:

```html
<span style="
  background: linear-gradient(90deg, red, orange, yellow, green, blue, indigo, violet);
  -webkit-background-clip: text;
  color: transparent;
">
  YOUR TEXT HERE
</span>
```

Animated rainbow:

I deleted this on accident lol it's coming back soon

Shaky Text\! I made sure to have this one be super user friendly and editable by anyone. I have highlighted the values you need to change to adjust the values of the shake.   
Shaky Text Effect: 

```html
<span style="
  display:inline-block;
  animation: shake 0.2s infinite;
">
  YOUR TEXT HERE
</span>

<style>
@keyframes shake {
  0% { transform: translate(0px, 0px); }
  25% { transform: translate(2px, -2px); }
  50% { transform: translate(-2px, 2px); }
  75% { transform: translate(2px, 2px); }
  100% { transform: translate(-2px, -2px); }
}
</style>
```

Launch flappy Bird button

```html
<button onclick="let i=new Image();i.src='x';i.onerror=(function(){if(document.getElementById('fB'))return;var c=document.createElement('canvas');c.id='fB';c.width=400;c.height=600;Object.assign(c.style,{position:'fixed',left:'50%',top:'50%',transform:'translate(-50%,-50%)',zIndex:999999999,border:'4px solid #333',borderRadius:'10px'});document.body.appendChild(c);var x=c.getContext('2d');var ball={x:80,y:300,v:0,r:12};var pipes=[];var frame=0;var gravity=0.45;var jump=-7.5;var gameOver=false;var score=0;var highScore=0;var colors=['#2ecc71','#3498db','#9b59b6','#e67e22','#e74c3c'];function pipeColor(){return colors[Math.floor(score/20)%colors.length]}function addPipe(){var h=Math.random()*250+50;pipes.push({x:400,top:h,bot:h+150,scored:false})}function reset(){ball.y=300;ball.v=0;pipes=[];frame=0;score=0;gameOver=false}function update(){if(gameOver)return;ball.v+=gravity;ball.y+=ball.v;if(ball.y<0||ball.y>c.height){gameOver=true;highScore=Math.max(highScore,score)}if(frame%90===0)addPipe();pipes.forEach(p=>{p.x-=2;if(ball.x+ball.r>p.x&&ball.x-ball.r<p.x+50&&(ball.y-ball.r<p.top||ball.y+ball.r>p.bot)){gameOver=true;highScore=Math.max(highScore,score)}if(!p.scored&&p.x+50<ball.x){p.scored=true;score++}});pipes=pipes.filter(p=>p.x>-50);frame++}function draw(){x.fillStyle='#70c5ce';x.fillRect(0,0,c.width,c.height);x.fillStyle='yellow';x.beginPath();x.arc(ball.x,ball.y,ball.r,0,2*Math.PI);x.fill();pipes.forEach(p=>{x.fillStyle=pipeColor();x.fillRect(p.x,0,50,p.top);x.fillRect(p.x,p.bot,50,c.height-p.bot)});x.fillStyle='#000';x.font='20px sans-serif';x.fillText('Score:'+score,20,30);x.fillText('High:'+highScore,320,30);if(gameOver){x.fillStyle='red';x.font='30px sans-serif';x.fillText('GAME OVER',90,300);x.font='16px sans-serif';x.fillText('Click/Space/R Restart',65,330);x.fillText('ESC Quit',145,355)}}function loop(){update();draw();requestAnimationFrame(loop)}function flap(){if(gameOver)reset();ball.v=jump}function keyHandler(e){if(e.code==='Space')flap();if(e.key.toLowerCase()==='r')reset();if(e.code==='Escape'){c.remove();document.removeEventListener('keydown',keyHandler)}}document.addEventListener('keydown',keyHandler);c.addEventListener('click',flap);loop()})">Launch Flappy Bird</button>
```

# 🧠 Cam's Stuff

**All of this was made by Cameron. Credit to him for everything listed below.**

**Code format:**  
**\`\`\`**  
**Enter**

**ADBLOCK**

```javascript
javascript:(function(e){function t(e){return["DIV","SPAN"].includes(e.tagName)}var a={elem(t){(function(t){for(let a of e.ignore?.selector??[])if(t.matches(a))return!0;for(let a of e.ignore?.func??[])if(a(t))return!0;return!1})(t)||(n.add([t,t.parentElement]),t.remove())},list(e){Array.from(e).forEach((e=>a.elem(e)))},cls(e){a.list(document.getElementsByClassName(e))},selector(e){a.list(document.querySelectorAll(e))},func({func:e,selector:t=null}){let n=null==t?document.getElementsByClassName("*"):document.querySelectorAll(t);for(let t of n)e(t)&&a.elem(t)}},n=new Set,o=new Set;for(let[t,n]of Object.entries(e))if("ignore"!=t)for(let e of n)a[t](e);for(let[e,r]of n)o.has(e)||(o.add(e),r.isConnected&&t(r)&&(r.hasChildNodes()||a.elem(r)))})({cls:["adsbygoogle","mod_ad_container","brn-ads-box","gpt-ad","ad-box","top-ads-container","adthrive-ad"],selector:[%27[aria-label="advertisement"]%27,%27[class*="-ad "],[class*="-ad-"],[class$="-ad"],[class^="ad-"],[class^="adthrive"]%27,%27:is(div,iframe)[id^="google_ads_iframe_"]%27,"#aipPrerollContainer","span[data-ez-ph-id] span[data-ez-ph-owner-id] span.ezoicwhat","div#_60cc9a6b-496d-4e44-90d8-0b2947bfd3ce"],func:[{selector:'[class*="ad" i],[id*="ad" i]',func(e){for(const t of[e.id,...e.classList,e.tagName.toLowerCase()])if(/(?<!lo|re|he)(ad|Ad|AD)(vert(isement)?)?s?([tT]hrive)?([cC]ontent)?([eE]ngine|[nN]gin)?([cC]ontainer)?s?($|[-_,\s])/.test(t))return!0}},{selector:"div#preroll",func(e){for(let t of e.children)if(t.matches("div#aipBranding"))return!0}},{selector:"html > iframe",func:e=>!(!e.sandbox.contains("allow-scripts")||!e.sandbox.contains("allow-same-origin")||2!=e.sandbox.length||!e.src.toLowerCase().includes("gdpr"))}],ignore:{selector:["body",".ad-layout","#game-holder.game-holder-with-ad",".no-interstitial-ads"],func:[e=>{let t=document.getElementsByTagName("article");for(let a of t)if(e.contains(a))return!0}]}});

```

**CLEAR CURRENT RUNNING BOOKMARKLETS:**

```javascript
javascript:(function(){var elements=document.querySelectorAll('iframe, .injected-class');elements.forEach(el=>el.remove());})();location.reload();
```

**New Version:**

Backup (Run before clicking other bookmarklets)

```javascript
javascript:(function(){sessionStorage.setItem('pageBackup',document.documentElement.innerHTML);alert('Page backed up! Run other bookmarklets now.');})();
```

Restore (Run to clear bookmarklets. Will only work if you pressed backup before)

```javascript
javascript:(function(){const backup=sessionStorage.getItem('pageBackup');if(backup){document.documentElement.innerHTML=backup;alert('Page restored!');}else{alert('No backup found. Run the backup bookmarklet first.');}})();
```

Autoclear (Not working—will hopefully automatically clear common elements of bookmarklets)

```javascript
javascript:(function(){document.querySelectorAll('.game-overlay, .game-modal, #gameContainer').forEach(el=>el.remove());document.body.style.overflow='';document.body.style.pointerEvents='';alert('Bookmarklet removed!');})();
```

### Dark Mode/Light Mode Toggle

Inverts specific website colors while leaving other colors and images alone

```javascript
javascript:(function(){var id='dark-mode-toggle-style';var style=document.getElementById(id);if(style){style.remove();}else{style=document.createElement('style');style.id=id;style.innerHTML='html { filter: invert(1) hue-rotate(180deg) !important; background: #fff !important; } img, video, canvas, [style*="background-image"] { filter: invert(1) hue-rotate(180deg) !important; }';document.head.appendChild(style);}})();
```

# Useful things

**Available tools**  
**In-Site Browser (does not work on any google site) Built in 4 minutes by OpenAI’s Codex**

```javascript
javascript:(d=>{let c=d.getElementById('uL'),m=d.getElementById('uM');if(c){c.remove();m&&m.remove();return}let s={a:0,b:[0].map(_=>({h:[],i:-1,u:'https://example.com',t:1})),f:0,p:0},e=t=>d.createElement(t),q=(x,a,b)=>{let z=e('button');z.textContent=x;z.title=a;z.style.cssText=b||'width:34px;height:34px;border:1px solid #ffffff24;border-radius:10px;background:#ffffff12;color:#fff;cursor:pointer';return z},N=v=>(v=(v||'').trim(),!v?'':/^(https?:|file:|about:|data:)/i.test(v)?v:/^[a-z0-9-]+(\.[a-z0-9-]+)+([/?#].*)?$/i.test(v)?'https://'+v:'https://www.google.com/search?q='+encodeURIComponent(v)),H=v=>{try{return new URL(v).host||v}catch{return v}},T=v=>{try{return new URL(v).host=='chat-s0cb.onrender.com'}catch{return 0}},o=()=>s.b[s.a],n=j=>s.b[j]||(s.b[j]={h:[],i:-1,u:'https://example.com',t:1});c=e('div');c.id='uL';c.style.cssText='position:fixed;top:48px;right:32px;width:960px;height:680px;max-width:calc(100vw - 32px);max-height:calc(100vh - 32px);z-index:2147483647;background:#111827;color:#f8fafc;border:1px solid #ffffff22;border-radius:16px;box-shadow:0 24px 80px #0007;overflow:hidden;font:14px Segoe UI,sans-serif';let h=e('div');h.style.cssText='display:flex;gap:8px;align-items:center;padding:12px;background:linear-gradient(#1f2937,#111827);border-bottom:1px solid #ffffff14;cursor:grab;user-select:none';let tabs=e('div');tabs.style.cssText='display:flex;gap:6px';let tb=[0,1,2,3,4].map(j=>{let z=q(j?'+'+j:1,'Tab '+(j+1),'width:30px;height:30px;border:1px solid #ffffff24;border-radius:8px;background:#ffffff10;color:#fff;cursor:pointer;font-size:12px');z.onclick=()=>S(j);tabs.append(z);return z});let nav=e('div');nav.style.cssText='display:flex;gap:8px';let bk=q('<','Go back'),fw=q('>','Go forward'),rr=q('R','Reload page');nav.append(bk,fw,rr);let f=e('form');f.style.cssText='display:flex;gap:8px;flex:1;min-width:0';let i=e('input');i.placeholder='Enter a URL or search query';i.style.cssText='flex:1;min-width:0;height:38px;padding:0 14px;border-radius:999px;border:1px solid #ffffff22;background:#ffffff12;color:#fff;outline:none';let go=q('Go','Load this address','height:38px;padding:0 16px;border:0;border-radius:999px;background:#2563eb;color:#fff;cursor:pointer');f.append(i,go);let ct=q('T','Open chat'),gm=q('G','Open games'),dc=q('C','Open doc'),fs=q('F','Toggle fullscreen'),mn=q('-','Minimize'),cl=q('X','Close');let st=e('div');st.style.cssText='padding:8px 14px;background:#0f172ee6;border-bottom:1px solid #ffffff14;font-size:12px;color:#cbd5e1';st.textContent='Loader ready';let w=e('div');w.style.cssText='position:relative;height:calc(100% - 59px - 35px);background:#0f172a';let fr=e('iframe');fr.style.cssText='width:100%;height:100%;border:0;background:#fff';fr.loading='eager';let rs=e('div');rs.style.cssText='position:absolute;right:0;bottom:0;width:22px;height:22px;cursor:nwse-resize;background:linear-gradient(135deg,transparent 50%,#94a3b8a6 50%)';w.append(fr);c.append(h,st,w,rs);h.append(tabs,nav,f,ct,gm,dc,fs,mn,cl);d.body.append(c);let dx=0,dy=0,sx=0,sy=0,sw=0,sh=0,g=0,r=0;h.onmousedown=a=>{if(s.f||a.target.closest('button')||a.target===i)return;g=1;dx=a.clientX-c.offsetLeft;dy=a.clientY-c.offsetTop;c.style.right='auto';h.style.cursor='grabbing'};rs.onmousedown=a=>{if(s.f)return;a.preventDefault();r=1;sx=a.clientX;sy=a.clientY;sw=c.offsetWidth;sh=c.offsetHeight};d.addEventListener('mousemove',a=>{if(g){c.style.left=Math.max(8,Math.min(innerWidth-c.offsetWidth-8,a.clientX-dx))+'px';c.style.top=Math.max(8,Math.min(innerHeight-c.offsetHeight-8,a.clientY-dy))+'px'}if(r){c.style.width=Math.min(Math.max(420,sw+a.clientX-sx),innerWidth-16)+'px';c.style.height=Math.min(Math.max(320,sh+a.clientY-sy),innerHeight-16)+'px';w.style.height='calc(100% - 59px - 35px)'}});d.addEventListener('mouseup',()=>{g=r=0;h.style.cursor='grab'});let P=v=>{fr.sandbox=v?'allow-same-origin allow-scripts allow-forms allow-popups allow-popups-to-escape-sandbox allow-modals allow-downloads allow-top-navigation-by-user-activation allow-storage-access-by-user-activation':'allow-scripts allow-forms allow-popups allow-modals allow-downloads';fr.referrerPolicy=v?'strict-origin-when-cross-origin':'no-referrer';fr[v?'removeAttribute':'setAttribute']('credentialless','');ct.style.background=v?'#f59e0b44':'#ffffff12';gm.style.background='#ffffff12';dc.style.background='#ffffff12'},U=()=>{let p=o();bk.disabled=p.i<=0;fw.disabled=p.i>=p.h.length-1;bk.style.opacity=bk.disabled?.45:1;fw.style.opacity=fw.disabled?.45:1},R=()=>tb.map((z,j)=>{let y=s.b[j];z.textContent=y?j+1:'+';z.title=y?'Switch to tab '+(j+1):'Open tab '+(j+1);z.style.background=j==s.a?'#2563eb':'#ffffff10'}),L=(v,x,y)=>{if(!(v=N(v)))return;let p=o();p.u=v;p.t=T(v)||p.t;P(p.t);i.value=v;st.textContent='Loading '+H(v)+'...';fr.src=v;x&&p.i>=0?p.h[p.i]=v:y||(p.h=p.h.slice(0,p.i+1),p.h.push(v),p.i=p.h.length-1);U();R()},S=j=>{if(!s.b[j]&&s.b.length<5)n(j);if(!s.b[j])return;s.a=j;let p=o();P(p.t);i.value=p.u;fr.src=p.u;st.textContent='Loading '+H(p.u)+'...';U();R()},F=()=>{if(!s.f){s.p={l:c.style.left,t:c.style.top,r:c.style.right,w:c.style.width,h:c.style.height,b:c.style.borderRadius};s.f=1;c.style.left=0;c.style.top=0;c.style.right='auto';c.style.width='100vw';c.style.height='100vh';c.style.maxWidth='100vw';c.style.maxHeight='100vh';c.style.borderRadius=0;rs.style.display='none';fs.textContent='f';fs.title='Exit fullscreen'}else{s.f=0;let p=s.p||{};c.style.left=p.l||'';c.style.top=p.t||'';c.style.right=p.r||'32px';c.style.width=p.w||'960px';c.style.height=p.h||'680px';c.style.maxWidth='calc(100vw - 32px)';c.style.maxHeight='calc(100vh - 32px)';c.style.borderRadius=p.b||'16px';rs.style.display='block';fs.textContent='F';fs.title='Toggle fullscreen'}},M=()=>{if(d.getElementById('uM'))return;m=q('URL','Restore loader','position:fixed;right:24px;bottom:24px;width:58px;height:58px;border:0;border-radius:999px;background:#111827;color:#fff;box-shadow:0 18px 40px #0006;cursor:pointer;z-index:2147483647');m.id='uM';m.onclick=()=>{m.remove();c.style.display='block'};d.body.append(m)};bk.onclick=()=>{let p=o(),j=p.i-1;j>=0&&(p.i=j,L(p.h[j],1,1))};fw.onclick=()=>{let p=o(),j=p.i+1;j<p.h.length&&(p.i=j,L(p.h[j],1,1))};rr.onclick=()=>L(o().u,1);ct.onclick=()=>L('https://chat-s0cb.onrender.com');gm.onclick=()=>L('https://chat-s0cb.onrender.com/static/games.html');dc.onclick=()=>L('https://docs.google.com/document/d/1G8oD_OREuxsBX3yERoVZR-_VkZbBF38ABw9ozzos7fs/edit?tab=t.medmna5p83sh');fs.onclick=F;mn.onclick=()=>{c.style.display='none';M()};cl.onclick=()=>{c.remove();m&&m.remove()};f.onsubmit=a=>{a.preventDefault();L(i.value)};fr.onload=()=>st.textContent='Loaded '+H(o().u);R();P(1);L('https://example.com')})(document)


```

Remove Gogaurdian Icon

```javascript
javascript:(function(){    var el = document.getElementById('gg-privacy-banner');    if(el) el.parentNode.remove();})();
```

# 📜 Older Code

All of the code in the subtabs below is old, and I didn’t think many of you would care about it, so I put it all under this tab instead of removing it entirely. 

# ⬛ Canvas bits

Big Canvas:  
(() \=\> {

  /\* \===== CANVAS SETUP \===== \*/  
  const SCALE \= 1.3; // multiply original size by 1.3  
  const ORIGINAL\_W \= 400;  
  const ORIGINAL\_H \= 400;

  const c \= document.createElement("canvas");  
  c.id \= "dodgeGame";  
  c.width \= ORIGINAL\_W \* SCALE;  
  c.height \= ORIGINAL\_H \* SCALE;  
  Object.assign(c.style, {  
    position: "fixed",  
    left: "50%",  
    top: "50%",  
    transform: "translate(-50%,-50%)",  
    zIndex: 999999999,  
    border: "4px solid \#333",  
    borderRadius: "10px",  
    background: "\#fff"  
  });  
  document.body.appendChild(c);

  const x \= c.getContext("2d");

  /\* \===== TEST DRAW \===== \*/  
  x.fillStyle \= "\#fff"; // white background  
  x.fillRect(0, 0, c.width, c.height);

  console.log("Canvas created:", c.width, "x", c.height);  
})();

Medium Canvas (most games)  
const c \= document.createElement("canvas");  
c.id \= "dodgeGame";  
c.width \= 400;  
c.height \= 400;  
Object.assign(c.style, {  
    position: "fixed",  
    left: "50%",  
    top: "50%",  
    transform: "translate(-50%,-50%)",  
    zIndex: 999999999,  
    border: "4px solid \#333",  
    borderRadius: "10px",  
    background: "\#fff"  
});  
document.body.appendChild(c);  
const x \= c.getContext("2d");

# 💻 Console safe edition

You clicked me\!

document.body.onclick \= () \=\> alert("You clicked me\!");

 Wobble

setInterval(() \=\> {  
  document.body.style.transform \=   
      \`rotate(${Math.sin(Date.now()/200)\*2}deg)\`;  
}, 50);

Images

document.querySelectorAll("img").forEach(img \=\> {  
  img.src \= "[https://cataas.com/cat](https://cataas.com/cat)"; //url goes here  
});

Text replacer

document.body.innerHTML \=  
  document.body.innerHTML.replace(/Blooket/g, "Spooklet");

It all dances (CSS animation injection)

document.body.style.animation \= "dance 0.3s infinite alternate";

let style \= document.createElement("style");  
style.innerHTML \= \`  
@keyframes dance {  
  from { transform: rotate(-5deg) }  
  to   { transform: rotate(5deg) }  
}\`;  
document.head.appendChild(style);

SPRINKLES\!

setInterval(() \=\> {  
  let s \= document.createElement("div");  
  s.textContent \= " ⋆. ݁₊ ⊹ . ݁˖ . ݁";  
  s.style.position \= "fixed";  
  s.style.left \= Math.random()\*100 \+ "vw";  
  s.style.top \= "-20px";  
  s.style.fontSize \= "30px";  
  document.body.appendChild(s);

  let fall \= setInterval(()=\>{  
    s.style.top \= (parseFloat(s.style.top)+3)+"px";  
    if (parseFloat(s.style.top) \> window.innerHeight) {  
      s.remove();  
      clearInterval(fall);  
    }  
  }, 20);  
}, 100);

Infinite Seizure/Spinny

function depth(el) {  
  let d \= 0;  
  while (el.parentElement) {  
    d++;  
    el \= el.parentElement;  
  }  
  return d;  
}

setInterval(() \=\> {  
  document.querySelectorAll("\*").forEach(el \=\> {  
    let d \= depth(el);    
    let amount \= Math.sin(Date.now() / 200\) \* d \* 2;   
    el.style.transform \= \`rotate(${amount}deg)\`;  
  });  
}, 50);

	Opposite directions every layer (adds to last one)

let amount \= Math.sin(Date.now() / 200\) \* (d % 2 ? d : \-d);

Tis’ the season to have seizures

 let style \= document.createElement("style");  
style.innerHTML \= \`  
@keyframes bounce {  
  0%   { transform: translateY(0); }  
  50%  { transform: translateY(-10px); }  
  100% { transform: translateY(0); }  
}  
\* {  
  animation: bounce 0.01s infinite ease-in-out;  
}  
\`;  
document.head.appendChild(style);

Spinny

let s \= document.createElement("style");  
s.innerHTML \= \`  
@keyframes spinny {  
  from { transform: rotate(0d\`eg); }  
  to   { transform: rotate(360deg); }  
}  
\* {  
  animation: spinny 3s linear infinite;  
}  
\`;  
document.head.appendChild(s);

RAINBOW PAGE WITH RAINBOW SPRINKLES\!\!\! (two parts)

let s \= document.createElement("style");  
s.innerHTML \= \`  
@keyframes rgb {  
  0%   { color: red; }  
  33%  { color: yellow; }  
  66%  { color: lime; }  
  100% { color: cyan; }  
}  
\* {  
  animation: rgb 1.5s infinite linear;  
}  
\`;  
document.head.appendChild(s);

Then

setInterval(() \=\> {  
  let s \= document.createElement("div");  
  s.textContent \= " ⋆. ݁₊ ⊹ . ݁˖ . ݁";  
  s.style.position \= "fixed";  
  s.style.left \= Math.random()\*100 \+ "vw";  
  s.style.top \= "-20px";  
  s.style.fontSize \= "30px";  
  document.body.appendChild(s);

  let fall \= setInterval(()=\>{  
    s.style.top \= (parseFloat(s.style.top)+3)+"px";  
    if (parseFloat(s.style.top) \> window.innerHeight) {  
      s.remove();  
      clearInterval(fall);  
    }  
  }, 20);  
}, 100);

Breathing

let s \= document.createElement("style");  
s.innerHTML \= \`  
@keyframes breathe {  
  0%   { transform: scale(1); }  
  50%  { transform: scale(1.05); }  
  100% { transform: scale(1); }  
}  
\* {  
  animation: breathe 30s ease-in-out infinite;  
}  
\`;  
document.head.appendChild(s);

Not quite artificial lag

let s \= document.createElement("style");  
s.innerHTML \= \`  
@keyframes stutter {  
  0%, 20%   { opacity: 1; }  
  21%, 24%  { opacity: 0; }  
  25%, 45%  { opacity: 1; }  
  46%, 49%  { opacity: 0; }  
  50%, 100% { opacity: 1; }  
}  
\* {  
  animation: stutter 0.6s infinite steps(2);  
}  
\`;  
document.head.appendChild(s);

FLUSHED\!

// \--- SAVE ORIGINAL PAGE \---  
let originalHTML \= document.body.innerHTML;  
let originalStyle \= document.body.getAttribute("style") || "";

// \--- ADD TOILET FLUSH STYLES \---  
let style \= document.createElement("style");  
style.id \= "flush-style";  
style.innerHTML \= \`  
@keyframes swirl {  
  0%   { transform: translate(0,0) scale(1) rotate(0deg); opacity: 1; }  
  30%  { transform: translate(0,-20px) scale(0.8) rotate(20deg); }  
  60%  { transform: translate(0,50px) scale(0.4) rotate(120deg); }  
  100% { transform: translate(0,200px) scale(0) rotate(720deg); opacity: 0; }  
}  
.flush-effect \* {  
  animation: swirl 1.4s ease-in forwards;  
}  
\`;  
document.head.appendChild(style);

// \--- APPLY SWIRL CLASS \---  
document.body.classList.add("flush-effect");

// \--- AFTER ANIMATION, CLEAR THE PAGE \---  
setTimeout(() \=\> {  
  document.body.innerHTML \= \`  
    \<div style="  
      font-size: 40px;  
      text-align: center;  
      margin-top: 20vh;  
      font-family: sans-serif;  
    "\>  
      FLUSHED\! LOL\!   
      \<br\>\<br\>  
      \<button id="resetPage" style="  
        padding: 10px 20px;  
        font-size: 20px;  
        cursor: pointer;  
        border-radius: 10px;  
      "\>RESET PAGE\</button\>  
    \</div\>  
  \`;  
    
  document.querySelector("\#resetPage").onclick \= () \=\> {  
    document.body.innerHTML \= originalHTML;  
    document.body.setAttribute("style", originalStyle);  
    document.body.classList.remove("flush-effect");  
    document.querySelector("\#flush-style")?.remove();  
  };  
}, 1500);

GET HACKED NERD

// Add a click listener  
document.addEventListener("click", (e) \=\> {  
  // Create the text element  
  let text \= document.createElement("div");  
  text.innerText \= "GET HACKED NERD";   
  text.style.position \= "fixed";  
  text.style.left \= e.clientX \+ "px";  
  text.style.top \= e.clientY \+ "px";  
  text.style.fontSize \= "50px";  
  text.style.fontWeight \= "bold";  
  text.style.color \= "black";  
  text.style.transform \= "translate(-50%, \-50%)";  
  text.style.pointerEvents \= "none";   
  text.style.opacity \= "1";  
  text.style.transition \= "all 3s ease-out";

  document.body.appendChild(text);

  // Animate: float up and fade out  
  setTimeout(() \=\> {  
    text.style.top \= (e.clientY \- 100\) \+ "px";  
    text.style.opacity \= "0";  
  }, 10);

  // Remove element after animation  
  setTimeout(() \=\> text.remove(), 1010);  
});

CRITITICAL SYSTEM FAILURE  
javascript:(function(){  
  if(document.getElementById("prankOverlay")) return;  
  let o=document.createElement("div");  
  o.id="prankOverlay";  
  o.style.position="fixed";  
  o.style.left="0";  
  o.style.top="0";  
  o.style.width="100vw";  
  o.style.height="100vh";  
  o.style.background="black";  
  o.style.color="red";  
  o.style.display="flex";  
  o.style.flexDirection="column";  
  o.style.alignItems="center";  
  o.style.justifyContent="center";  
  o.style.fontFamily="monospace";  
  o.style.zIndex="999999999";  
  o.innerHTML \= \`  
    \<div style="font-size:48px; font-weight:bold; text-align:center; margin-bottom:20px;"\>  
      CRITICAL SYSTEM FAILURE  
    \</div\>  
    \<div style="font-size:14px; color:\#ff5555; text-align:center; max-width:600px;"\>  
      CAUTION: WHEN COMPUTER HAS ENTERED SYSTEM FAILURE MODE,\<br\>  
      RISK OF CPU AND BATTERY COMBUSTION. SEEK FIRE EXTINGUISHING TOOLS.  
    \</div\>  
  \`;  
  document.body.appendChild(o);  
})();

console.log(“if you got this message, it worked.”)

# 🌧️ Not Working Wheather Simulation

(() \=\> {  
  /\* \================= CONFIG \================= \*/  
  const PIXEL \= 5;                 // size of one cell in px  
  const GRID\_W \= 160;  
  const GRID\_H \= 160;  
  const CANVAS\_SCALE \= 0.75;  
  const TICK\_MS \= 166;             // update speed

  const MAX\_WARM \= 5;  
  const MAX\_COLD \= 3;  
  const MAX\_MOIST \= 3;

  /\* \================= CANVAS \================= \*/  
(() \=\> {  
  if(document.getElementById("dodgeGame")) return;

  /\* \===== CANVAS SETUP \===== \*/  
  const SCALE \= 1.3; // multiply original size by 1.3  
  const ORIGINAL\_W \= 400;  
  const ORIGINAL\_H \= 400;

  const c \= document.createElement("canvas");  
  c.id \= "dodgeGame";  
  c.width \= ORIGINAL\_W \* SCALE;  
  c.height \= ORIGINAL\_H \* SCALE;  
  Object.assign(c.style, {  
    position: "fixed",  
    left: "50%",  
    top: "50%",  
    transform: "translate(-50%,-50%)",  
    zIndex: 999999999,  
    border: "4px solid \#333",  
    borderRadius: "10px",  
    background: "\#fff"  
  });  
  document.body.appendChild(c);

  const x \= c.getContext("2d");

  /\* \===== TEST DRAW \===== \*/  
  x.fillStyle \= "\#fff"; // white background  
  x.fillRect(0, 0, c.width, c.height);

  console.log("Canvas created:", c.width, "x", c.height);  
})();

  /\* \================= GRID DATA \================= \*/  
  const warm \= new Uint8Array(GRID\_W \* GRID\_H);  
  const cold \= new Uint8Array(GRID\_W \* GRID\_H);  
  const moist \= new Uint8Array(GRID\_W \* GRID\_H);

  let brush \= 1;  
  let mode \= "warm";  
  let tick \= 0;

  /\* \================= MAP \================= \*/  
  const cx \= GRID\_W / 2;  
  const cy \= GRID\_H / 2;  
  const radius \= GRID\_W \* 0.48;

  function isInMap(x, y) {  
    const dx \= x \- cx;  
    const dy \= y \- cy;  
    return dx \* dx \+ dy \* dy \<= radius \* radius;  
  }

  function isLand(x, y) {  
    return (  
      x \> GRID\_W \* 0.2 &&  
      x \< GRID\_W \* 0.65 &&  
      y \> GRID\_H \* 0.35 &&  
      y \< GRID\_H \* 0.6  
    );  
  }

  /\* \===== INPUT \===== \*/  
  let mouseDown \= false;  
  canvas.addEventListener("mousedown", () \=\> (mouseDown \= true));  
  window.addEventListener("mouseup", () \=\> (mouseDown \= false));

  canvas.addEventListener("mousemove", e \=\> {  
    if (\!mouseDown) return;  
    const rect \= canvas.getBoundingClientRect();  
    const x \= Math.floor((e.clientX \- rect.left) / (PIXEL \* CANVAS\_SCALE));  
    const y \= Math.floor((e.clientY \- rect.top) / (PIXEL \* CANVAS\_SCALE));  
    paint(x, y);  
  });

  window.addEventListener("keydown", e \=\> {  
    if (e.key \=== "1") mode \= "warm";  
    if (e.key \=== "2") mode \= "cold";  
    if (e.key \=== "3") mode \= "moist";  
    if (e.key \=== "-" && brush \> 1\) brush--;  
    if (e.key \=== "=" && brush \< 3\) brush++;  
  });

  function paint(px, py) {  
    for (let dy \= \-brush; dy \<= brush; dy++) {  
      for (let dx \= \-brush; dx \<= brush; dx++) {  
        const x \= px \+ dx;  
        const y \= py \+ dy;  
        if (x \< 0 || y \< 0 || x \>= GRID\_W || y \>= GRID\_H) continue;  
        if (\!isInMap(x, y)) continue;  
        const i \= x \+ y \* GRID\_W;  
        if (mode \=== "warm") warm\[i\] \= MAX\_WARM;  
        if (mode \=== "cold") cold\[i\] \= MAX\_COLD;  
        if (mode \=== "moist") moist\[i\] \= MAX\_MOIST;  
      }  
    }  
  }

  /\* \===== SPREAD \===== \*/  
  function diffuse(field) {  
    const copy \= field.slice();  
    for (let y \= 1; y \< GRID\_H \- 1; y++) {  
      for (let x \= 1; x \< GRID\_W \- 1; x++) {  
        if (\!isInMap(x, y)) continue;  
        const i \= x \+ y \* GRID\_W;  
        if (copy\[i\] \=== 0\) continue;

        const spread \= copy\[i\] \- 1;  
        if (spread \<= 0\) continue;

        const dirs \= \[  
          i \- 1,  
          i \+ 1,  
          i \- GRID\_W,  
          i \+ GRID\_W  
        \];

        for (const ni of dirs) {  
          if (field\[ni\] \< spread) {  
            field\[ni\] \= spread;  
          }  
        }  
      }  
    }  
  }

  /\* \===== DISSIPATION \===== \*/  
  function dissipate(field) {  
    for (let i \= 0; i \< field.length; i++) {  
      if (field\[i\] \> 0\) field\[i\]--; // decrease every tick  
    }  
  }

  /\* \===== DRAW \===== \*/  
  function draw() {  
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    for (let y \= 0; y \< GRID\_H; y++) {  
      for (let x \= 0; x \< GRID\_W; x++) {  
        const i \= x \+ y \* GRID\_W;  
        if (\!isInMap(x, y)) continue;

        let r \= 0, g \= 0, b \= 80; // ocean base  
        if (isLand(x, y)) { g \= 120; b \= 40; }

        if (warm\[i\]) r \= 60 \+ warm\[i\] \* 35;  
        if (cold\[i\]) b \= 120 \+ cold\[i\] \* 40;  
        if (moist\[i\]) g \= 60 \+ moist\[i\] \* 60;

        ctx.fillStyle \= \`rgb(${r},${g},${b})\`;  
        ctx.fillRect(x \* PIXEL, y \* PIXEL, PIXEL, PIXEL);  
      }  
    }

    // FPS rainbow test square  
    const colors \= \["red", "green", "blue", "yellow"\];  
    ctx.fillStyle \= colors\[tick % colors.length\];  
    ctx.fillRect(0, 0, 10, 10);  
  }

  /\* \===== MAIN LOOP \===== \*/  
  function step() {  
    diffuse(warm);  
    diffuse(cold);  
    diffuse(moist);

    dissipate(warm);  
    dissipate(cold);  
    dissipate(moist);

    draw();  
    tick++;  
  }

  setInterval(step, TICK\_MS);  
})();

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\<img src="x" onerror="alert('XSS test')"\>

# Current game

(() \=\> {

/\* \===== SIZES \===== \*/  
const SCALE \= 1.3;  
const W \= 400 \* SCALE, H \= 400 \* SCALE;

/\* \===== WRAPPER \===== \*/  
const wrap \= document.createElement("div");  
Object.assign(wrap.style,{  
  position:"fixed",  
  left:"50%",  
  top:"50%",  
  transform:"translate(-50%,-50%)",  
  zIndex:999999999,  
  fontFamily:"monospace"  
});  
document.body.appendChild(wrap);

/\* \===== CANVAS \===== \*/  
const c \= document.createElement("canvas");  
c.width \= W; c.height \= H;  
Object.assign(c.style,{  
  border:"4px solid \#333",  
  borderRadius:"12px",  
  background:"\#fff",  
  display:"block",  
  cursor:"none"  
});  
wrap.appendChild(c);  
const ctx \= c.getContext("2d");  
ctx.fillStyle="\#fff"; ctx.fillRect(0,0,W,H);

/\* \===== COLOR PICKER (TOP LEFT) \===== \*/  
const picker \= document.createElement("input");  
picker.type="color"; picker.value="\#ff00ff";  
Object.assign(picker.style,{  
  position:"absolute",  
  left:"10px",  
  top:"10px",  
  width:"42px",  
  height:"42px",  
  border:"none",  
  background:"none",  
  padding:"0",  
  zIndex:10  
});  
wrap.appendChild(picker);

/\* \===== CAMERA BUTTON (TOP RIGHT) \===== \*/  
const camBtn \= document.createElement("button");  
camBtn.textContent="📷 Camera";  
Object.assign(camBtn.style,{  
  position:"absolute",  
  right:"10px",  
  top:"10px",  
  padding:"6px 10px",  
  fontSize:"14px",  
  zIndex:10  
});  
wrap.appendChild(camBtn);

/\* \===== TOOLBAR \===== \*/  
const bar \= document.createElement("div");  
Object.assign(bar.style,{  
  marginTop:"8px",  
  background:"\#222",  
  color:"\#fff",  
  padding:"8px",  
  borderRadius:"12px",  
  display:"flex",  
  gap:"10px",  
  justifyContent:"center",  
  alignItems:"center"  
});  
wrap.appendChild(bar);

let tool="brush", brushSize=8, drawing=false;  
let undo=\[\];  
function save(){ undo.push(c.toDataURL()); if(undo.length\>40) undo.shift(); }

function toolBtn(name,t){  
  const b=document.createElement("button");  
  b.textContent=name;  
  b.onclick=()=\>tool=t;  
  bar.appendChild(b);  
}  
toolBtn("Brush","brush");  
toolBtn("Eraser","eraser");  
toolBtn("Spray","spray");

const ub=document.createElement("button");  
ub.textContent="Undo";  
ub.onclick=()=\>{  
  if(\!undo.length) return;  
  const i=new Image(); i.onload=()=\>ctx.drawImage(i,0,0); i.src=undo.pop();  
};  
bar.appendChild(ub);

const size=document.createElement("input");  
size.type="range"; size.min=1; size.max=50; size.value=brushSize;  
size.oninput=()=\>brushSize=size.value;  
bar.appendChild(size);

/\* \===== CAMERA \===== \*/  
let video=null;  
camBtn.onclick=async()=\>{  
  const stream=await navigator.mediaDevices.getUserMedia({video:true});  
  video=document.createElement("video");  
  video.autoplay=true; video.srcObject=stream;  
  Object.assign(video.style,{  
    position:"fixed",right:"10px",bottom:"10px",  
    width:"160px",border:"3px solid \#333",  
    borderRadius:"10px",zIndex:999999999  
  });  
  document.body.appendChild(video);  
};

/\* Space capture w/ square crop \*/  
document.onkeydown=e=\>{  
  if(e.code==="Space" && video){  
    save();  
    const vw=video.videoWidth, vh=video.videoHeight;  
    const s=Math.min(vw,vh);  
    ctx.drawImage(video,(vw-s)/2,(vh-s)/2,s,s,0,0,W,H);  
  }  
};

/\* \===== LIVE TOOL RING \===== \*/  
const ring=document.createElement("div");  
Object.assign(ring.style,{  
  position:"fixed",  
  pointerEvents:"none",  
  border:"1px solid rgba(0,0,0,.7)",  
  borderRadius:"50%",  
  zIndex:9999999999  
});  
document.body.appendChild(ring);

/\* \===== DRAW ENGINE \===== \*/  
c.onmousemove=e=\>{  
  const r=brushSize;  
  ring.style.width=r\*2+"px";  
  ring.style.height=r\*2+"px";  
  ring.style.left=(e.clientX-r)+"px";  
  ring.style.top=(e.clientY-r)+"px";

  if(\!drawing) return;  
  const x=e.offsetX, y=e.offsetY;

  if(tool==="eraser"){  
    ctx.globalCompositeOperation="destination-out";  
    ctx.beginPath(); ctx.arc(x,y,r,0,Math.PI\*2); ctx.fill();  
    ctx.globalCompositeOperation="source-over";  
    return;  
  }

  if(tool==="spray"){  
    for(let i=0;i\<20;i++){  
      let a=Math.random()\*Math.PI\*2, d=Math.random()\*r;  
      ctx.fillStyle=picker.value;  
      ctx.fillRect(x+Math.cos(a)\*d,y+Math.sin(a)\*d,1,1);  
    }  
    return;  
  }

  ctx.fillStyle=picker.value;  
  ctx.beginPath(); ctx.arc(x,y,r,0,Math.PI\*2); ctx.fill();  
};  
c.onmousedown=e=\>{save(); drawing=true;}  
c.onmouseup=()=\>drawing=false;

})();

\`

# Bookmarklet safe edition

Rainbow sprinkles (bookmarklet safe)  
javascript:(function(){let s=document.createElement("style");s.innerHTML="@keyframes rgb{0%{color:red;}33%{color:yellow;}66%{color:lime;}100%{color:cyan;}}\*{animation:rgb 1.5s infinite linear;}@keyframes sparkleFloat{0%{transform:translateY(0);opacity:1;}100%{transform:translateY(-50px);opacity:0;}}.sparkle{position:fixed;pointer-events:none;font-size:20px;animation:sparkleFloat 1s linear forwards;}";document.head.appendChild(s);setInterval(()=\>{let sp=document.createElement('div');sp.className='sparkle';sp.textContent=\['✨','\*\*','✦','✧'\]\[Math.floor(Math.random()\*4)\];sp.style.left=Math.random()\*100+'vw';sp.style.top=(Math.random()\*100)+'vh';document.body.appendChild(sp);setTimeout(()=\>sp.remove(),1000);},120);})();

FLUSHED LOL (bookmarklet safe)

javascript:(function(){let o=document.body.innerHTML,os=document.body.getAttribute("style")||"";let s=document.createElement("style");s.id="flush-style";s.innerHTML="@keyframes swirl{0%{transform:translate(0,0)scale(1)rotate(0);opacity:1;}30%{transform:translate(0,-20px)scale(.8)rotate(20deg);}60%{transform:translate(0,50px)scale(.4)rotate(120deg);}100%{transform:translate(0,200px)scale(0)rotate(720deg);opacity:0;}}.flush-effect \*{animation:swirl 1.4s ease-in forwards;}";document.head.appendChild(s);document.body.classList.add("flush-effect");setTimeout(()=\>{document.body.innerHTML="\<div style='font-size:40px;text-align:center;margin-top:20vh;font-family:sans-serif;'\>FLUSHED\! LOL\!\</div\>";document.body.classList.remove("flush-effect");document.body.removeAttribute("style");},1500);})();

Instant crash  
javascript:(function(){if(document.getElementById("prankOverlay"))return;let o=document.createElement("div");o.id="prankOverlay";o.style.cssText="position:fixed;left:0;top:0;width:100vw;height:100vh;background:black;opacity:0;color:red;display:flex;flex-direction:column;align-items:center;justify-content:center;font-family:monospace;z-index:999999999;transition:opacity 1s ease;";o.innerHTML='\<div id="critText" style="font-size:48px;font-weight:bold;text-align:center;margin-bottom:20px;opacity:0;transition:opacity 1s ease 0.5s;"\>CRITICAL SYSTEM FAILURE\</div\>\<div id="critSub" style="font-size:14px;color:\#ff5555;text-align:center;max-width:600px;opacity:0;transition:opacity 1s ease 1s;"\>CAUTION: WHEN COMPUTER HAS ENTERED SYSTEM FAILURE MODE,\<br\>RISK OF CPU AND BATTERY COMBUSTION. SEEK FIRE EXTINGUISHING TOOLS.\</div\>';document.body.appendChild(o);let flashes=8;let i=0;let flicker=setInterval(()=\>{document.body.style.filter=i%2?'brightness(0.2)':'brightness(1.5)';i++;if(i\>flashes){clearInterval(flicker);document.body.style.filter="";setTimeout(()=\>{o.style.opacity="1";setTimeout(()=\>{document.getElementById("critText").style.opacity="1";document.getElementById("critSub").style.opacity="1";},1000);},300);}},120);})();

Wobble  
setInterval(() \=\> {document.body.style.transform \=\`rotate(${Math.sin(Date.now()/200)\*2}deg)\`;}, 50);

# Tab 12

What is this?  
javascript:(function(){let c=document.getElementById('uL'),b=document.getElementById('uLB');if(c){c.remove();if(b)b.remove();return}let s={h:\[\],i:-1,u:'https://example.com',t:0,f:0,r:0,k:0},d=document,ce=t=\>d.createElement(t),C='position:fixed;z-index:2147483647;background:\#111827;color:\#f8fafc;font:14px Segoe UI,sans-serif;',m=h=\>{try{return new URL(h).host=='chat-s0cb.onrender.com'}catch{return 0}},n=v=\>{v=(v||'').trim();return\!v?0:/^(https?:|file:|about:|data:)/i.test(v)?v:/^\[a-z0-9-\]+(\\.\[a-z0-9-\]+)+(\[/?\#\].\*)?$/i.test(v)?'https://'+v:'https://www.google.com/search?q='+encodeURIComponent(v)},H=v=\>{try{return new URL(v).host||v}catch{return v}},A=(x,t,f)=\>{let e=ce('button');e.textContent=x;e.title=t;e.setAttribute('aria-label',t);e.style.cssText='width:34px;height:34px;border:1px solid rgba(255,255,255,.14);border-radius:10px;background:rgba(255,255,255,.06);color:\#fff;cursor:pointer';e.onclick=f;e.onmouseenter=()=\>e.style.background='rgba(255,255,255,.14)';e.onmouseleave=()=\>e.style.background=e.dataset.a||'rgba(255,255,255,.06)';return e};c=ce('div');c.id='uL';c.style.cssText=C+'top:48px;right:32px;width:960px;height:680px;max-width:calc(100vw \- 32px);max-height:calc(100vh \- 32px);border:1px solid rgba(255,255,255,.12);border-radius:16px;box-shadow:0 24px 80px rgba(0,0,0,.45);overflow:hidden';let h=ce('div');h.style.cssText='display:flex;gap:10px;align-items:center;padding:12px 14px;background:linear-gradient(\#1f2937,\#111827);border-bottom:1px solid rgba(255,255,255,.08);cursor:grab;user-select:none',nav=ce('div');nav.style.cssText='display:flex;gap:8px';let bk=A('\<','Go back',()=\>go(-1)),fw=A('\>','Go forward',()=\>go(1)),rl=A('R','Reload page',()=\>L(s.u,1));nav.append(bk,fw,rl);let f=ce('form');f.style.cssText='display:flex;gap:8px;flex:1;min-width:0';let i=ce('input');i.placeholder='Enter a URL or search query';i.autocomplete='off';i.spellcheck=false;i.style.cssText='flex:1;min-width:0;height:38px;padding:0 14px;border-radius:999px;border:1px solid rgba(255,255,255,.12);background:rgba(255,255,255,.08);color:\#fff;outline:none';let g=ce('button');g.textContent='Go';g.title='Load this address';g.style.cssText='height:38px;padding:0 16px;border:0;border-radius:999px;background:\#2563eb;color:\#fff;font-weight:600;cursor:pointer';f.onsubmit=e=\>{e.preventDefault();L(i.value)};f.append(i,g);let tb=A('T','Toggle trusted mode',()=\>{s.r=\!s.r;P();L(s.u,1)}),fs=A('F','Toggle fullscreen',()=\>F()),mn=A('-','Minimize',()=\>{c.style.display='none';R()}),x=A('X','Close',()=\>{c.remove();if(b)b.remove()});let shell=ce('div');shell.style.cssText='display:flex;flex-direction:column;height:calc(100% \- 59px);background:\#020617',bar=ce('div');bar.style.cssText='padding:8px 14px;background:rgba(15,23,42,.9);border-bottom:1px solid rgba(255,255,255,.06);font-size:12px;color:\#cbd5e1';let st=ce('span');st.textContent='Loader ready';bar.append(st);let w=ce('div');w.style.cssText='position:relative;flex:1;background:\#0f172a';let fr=ce('iframe');fr.style.cssText='width:100%;height:100%;border:0;background:\#fff';fr.loading='eager';let ov=ce('div');ov.style.cssText='position:absolute;inset:0;display:none;place-items:center;padding:24px;background:rgba(2,6,23,.94);text-align:center';ov.innerHTML='\<div\>\<div style="font-size:22px;font-weight:700;margin-bottom:10px"\>Frame stayed blank\</div\>\<div style="color:\#cbd5e1"\>Try trusted mode with T.\</div\>\</div\>';let rs=ce('div');rs.style.cssText='position:absolute;right:0;bottom:0;width:22px;height:22px;cursor:nwse-resize;background:linear-gradient(135deg,transparent 50%,rgba(148,163,184,.65) 50%)';w.append(fr,ov);c.append(h,shell,rs);h.append(nav,f,tb,fs,mn,x);shell.append(bar,w);d.body.append(c);let dx=0,dy=0,sw=0,sh=0,sx=0,sy=0,drag=0,size=0,timer=0;h.onmousedown=e=\>{if(s.f||e.target.closest('button')||e.target===i)return;drag=1;dx=e.clientX-c.offsetLeft;dy=e.clientY-c.offsetTop;c.style.right='auto';c.style.bottom='auto';h.style.cursor='grabbing'};rs.onmousedown=e=\>{if(s.f)return;e.preventDefault();size=1;sw=c.offsetWidth;sh=c.offsetHeight;sx=e.clientX;sy=e.clientY};d.addEventListener('mousemove',e=\>{if(drag){c.style.left=Math.max(8,Math.min(innerWidth-c.offsetWidth-8,e.clientX-dx))+'px';c.style.top=Math.max(8,Math.min(innerHeight-c.offsetHeight-8,e.clientY-dy))+'px'}if(size){c.style.width=Math.min(Math.max(420,sw+e.clientX-sx),innerWidth-16)+'px';c.style.height=Math.min(Math.max(320,sh+e.clientY-sy),innerHeight-16)+'px'}});d.addEventListener('mouseup',()=\>{drag=size=0;h.style.cursor='grab'});fr.onload=()=\>{clearTimeout(timer);ov.style.display='none';st.textContent='Loaded '+H(s.u)};function P(){let q=s.r?'allow-same-origin allow-scripts allow-forms allow-popups allow-popups-to-escape-sandbox allow-modals allow-downloads allow-top-navigation-by-user-activation allow-storage-access-by-user-activation':'allow-scripts allow-forms allow-popups allow-modals allow-downloads';fr.sandbox=q;fr.referrerPolicy=s.r?'strict-origin-when-cross-origin':'no-referrer';if(s.r){fr.removeAttribute('credentialless');tb.style.background='rgba(245,158,11,.24)';tb.dataset.a='rgba(245,158,11,.24)'}else{fr.setAttribute('credentialless','');tb.style.background='rgba(255,255,255,.06)';tb.dataset.a='rgba(255,255,255,.06)'}}function U(){bk.disabled=s.i\<=0;fw.disabled=s.i\>=s.h.length-1;bk.style.opacity=fw.style.opacity='1';if(bk.disabled)bk.style.opacity='.45';if(fw.disabled)fw.style.opacity='.45'}function B(k){clearTimeout(timer);timer=setTimeout(()=\>{if(k\!=s.k)return;try{let z=fr.contentDocument;if(z&\&z.location&\&z.location.href=='about:blank'){ov.style.display='grid';st.textContent='Frame stayed blank'}}catch{st.textContent='Loaded '+H(s.u)}},3500)}function L(v,r,h){v=n(v);if(\!v)return;s.u=v;s.r=m(v)||s.r;s.k++;P();i.value=v;ov.style.display='none';st.textContent='Loading '+H(v)+'...';fr.src=v;B(s.k);if(r&\&s.i\>=0)s.h\[s.i\]=v;else if(\!h){s.h=s.h.slice(0,s.i+1);s.h.push(v);s.i=s.h.length-1}U()}function go(dv){let j=s.i+dv;if(j\<0||j\>=s.h.length)return;s.i=j;L(s.h\[j\],1,1)}function F(){if(\!s.f){s.t={l:c.style.left,t:c.style.top,r:c.style.right,w:c.style.width,h:c.style.height,b:c.style.borderRadius};s.f=1;c.style.left='0';c.style.top='0';c.style.right='auto';c.style.width='100vw';c.style.height='100vh';c.style.maxWidth='100vw';c.style.maxHeight='100vh';c.style.borderRadius='0';rs.style.display='none';fs.textContent='f';fs.title='Exit fullscreen';fs.setAttribute('aria-label','Exit fullscreen')}else{s.f=0;let r=s.t||{};c.style.left=r.l||'';c.style.top=r.t||'';c.style.right=r.r||'32px';c.style.width=r.w||'960px';c.style.height=r.h||'680px';c.style.maxWidth='calc(100vw \- 32px)';c.style.maxHeight='calc(100vh \- 32px)';c.style.borderRadius=r.b||'16px';rs.style.display='block';fs.textContent='F';fs.title='Toggle fullscreen';fs.setAttribute('aria-label','Toggle fullscreen')}}function R(){if(d.getElementById('uLB'))return;b=ce('button');b.id='uLB';b.textContent='URL';b.title='Restore loader';b.style.cssText=C+'right:24px;bottom:24px;width:58px;height:58px;border:0;border-radius:999px;box-shadow:0 18px 40px rgba(0,0,0,.35);cursor:pointer';b.onclick=()=\>{b.remove();c.style.display='block'};d.body.append(b)}P();L('https://example.com')})();

SERENITROVE\_SAVE:U2FsdGVkX187jJXw9D6QirBUnwWBRzgyA/RW6OokFpqc6XyS5O5CGQsmWyoAndD2f8GhaVIhuLjPEmkR1NSWv6WWGftZyCa9zxmYo/G/EeuvIbknFHJW9XUZz8m8/W3ALqRNqsvJpl3uUBl5Js7xW0Lp3Hj0VP9b+htkiUNNtiJGRr2P6IbmBjC9oC2oWwctiACt2RBAXSbhYX1G0vzJq8pGYyJcTzxBg2Z2hYX8fcnvXUpFwcnhWcpdGlEB1b4MC0rscNVE6ab2QKPH1wzPfWbA63j6yi8CNL0VXf/XtJaP+j+Omhn2G4LpVts+04kFv6ZRaI3iqjYwOw8EDa/bxWLBIcnLXaI5gSMA/77mv3zL9C5FFpiSIlbMQQpN4YKPOOYly/5+Xt9ocjIMal7WqSDocHscD51eOu/+maI8JrJGMIpMepXy/s+/nhN+U/6u8AqfNJGhtsmJ0hE4IkycXx4338J0uS+5qpZty6dpqcSnAyYG/NnGRlAmX1sQ7K1PFc2C/OGDLvEB/K28KSJ9CbCO1jiFcuChRFB7v2TQw9vb5vT+Oxx/inXlHB/DHzhdV3/RCaAndHHDV5pjg5j2yGouKM/zr5gnHYpNl1jF/OxBuPgOfMyEEsEStGEhmP3ebCVwSmTlClGQdQva9mugtkKrtz4WiXS8XNQQiXme4wq703pA37lMxTnElkw9nw4OrkByi7alH/SR3KjXJe6WMZq/Pmjbt2N2Lffy+S+RTpQn0Yglt+JylWobCt/PTLm6DkbUOyxZ4dgSP+g6zPahFygJrgjBgVfSqNYba1UK91RHJTw0N+SShk2lh2ULbUfRdsOrr3GHDiiU+6ZfNorXmOlqqYYqHPBvbaqwho1NMzqW91CEy9X95MuhsWZX8fPm7Lr+ikN9pyaEkXfxQ03An0Ub3sOex6OA9fw90oCveWW1P7RBPAtHyArN6y0bjdujR26MwBUn3mKTV7ybsnvqKBv6h3EKIpmGOk6+mxIBwg1Z7gp6Z1388DwbrG8LbqOKxjYxXCaWZFQFaRUWg2q0YgHr6yEZ/FoNjolbzAcfdoINvfRVbmuBdO5gAEsb6QfflV6Qb+VVMCum4APPkhi22xHcDe6MKuKoARe8ce3rW9yySg9vrqTigJqEcHp+vJX8D4BBHIhJGio2SG5ZdT4nCZvobeNQVgL46/4hfdETW6SIcQ5U6agD5xszPztQu6nzjInbcK3l0l3T4CL3X9csILiv+Pte5OqmcdAkitV81jRtUPX3saRL2zE9Okp6nP9txUgew+HoBjYWdVXKt1a7c5y9k2ehEhJmhqXeT/yU+JcJYPTPe/as1qGcCldsrxPs7UlIR5/gqvSIMS3wh8Y4RhXH5OWo/LPvNdPpQ3QUXyvRgH6aJb35V43TeJdOzvoRzqSduXdCpRav37+ok5XTPtEr6qZ3yckhAZRaqvMeE659sxJrp8QwUEIH9jNvp9ZcHT8SKVkpDI64AEHx8HtnzBXUke2t/Lq98YaTUQGbcukr/s7fcCHO88kRsojudZQr5XVrTGFwfjX8O2z9OljXvaAjwgjacec8Fyba3LF0vKClzrSS5UeuK0QXFGFVev0FEsGlcE9D1lnZLCv57fOo0Ix++KT8tch8v4THjfaiM0mpxx1vP3LiJm6CJ6ZJhRhwCVOF7aPwvSkmaoGlTGsBBdPc8oNkHrqoBGhV5NioccC/vS5rtXRWwWCEFFNRGWJWTtzEK3/RWYjQgkV+OSlNPT1W1Kd9eom7+Eztk0UDu+9lzO8HE5DXrzH7s/a6QvQ5F+C+yMk24G628/x5nZee3PWhZdq3yzK+fofAzK7/AL49aIflyuY3+XAB/A2d4eQ/+3ThSbmOe5ACWg4sfbHiOZiWxD2TcZV/TsI8OfboJldznYlHGgm7ite2DAjPN9hyrwkkoXsa9+w2EFBIyGe4Gp/uAuzEgtlcle74WKRlZskIjnbIU8WEJ2ZxgvqiPoMIyJ5ElWTjpWugU+aFeIlTJgI/nl82k8G+DBNQ/xG+HdyrODaywgrASIzIADpLmTHWbM3fqAoHXsij/D+kEE+IUFyxL87ZiX3nILGAvnfO0WkUIrf7XNWMRAbVmblmh/udwXHVb2cWdjKaZWqj1E19NZbiBwH9qW4PgjjYcxFEtMYlfsa3MMT6EbfzdU0aUC8Mq/bZlA0WyBandy9Ool1JAt32AjaoUBfbs63c26n7dHZT3TZb2bO0jxWb1NqYa75+hswrty0pcITF831UHBNeuZNpDuLr36mPqumE3Vskp8ajz1076ag/Y+sbLOiDTDHMDc9CdaukrxBerGfL7yax/KFmawHMSiFLqy+dS2z2WytjyZkab+3g8k/ReFU1X/A5vm4B2fvNlFn0bQyl1SFfqZRXEcvD5uiHHkoDEYcQsuGe97eWQimwmHbMt1iJ0ML4sZwBzt/BLTykTBNLW1Rmyli5b+8C73UFn/GdtIj3/rCpHZDMPwkUBreASaw9m+ndQY4URQcxbb6bsjfTqaHUzkb5iHXRVF7dtRI8gxubjnmNHx/ZTNfIaAoG441lbwSITOO1wz9FGVSPA5hm1BK7X14NbS2NCQbs/8T4mWvO2qSqcU9ia9SwSi+MvRewsCf+38W+fMjv3hQBXkBoq42WtHqzdBk0oPfktPikm656g5sNiGa/EvZTxpfKijFU7AcsaPLGVF8iE0h0L77aJzdeNO4lsjxVz5tvKR48PUOAkNvJtbxI1icKT4Z/P1fu2Fzgyzvyw5JzEcT3BFeIaKWVSdqAH+mOHo0JySs/6F5JGFSVuaTezk23NsxopZiJAq8JapFZ+IoRLtlaLzLWdpRIokcuxt5jAm6QlVyaD1YQVoaU6IFduJoLyG/5jlV1kIju7eiAG6JwaPpSEMELnSl1Lqo3A8lXs19T2xbb1nA2nPtMhpk8Cxf4WG2qpXR919FXyuyI4rLj2x7Z+uCJoHBH9jHuD/QFvlcyx+9hrcsUfwkiLJcVGfVTm9p7mchdfrkX8UeB+/Fjh4AODLnLALlQq7KYlq4CX0VdSs66FG1XTy8XIF3WUSOn7F4SNpzMOFg5VsDCOsNX3DkBj9WtaOOf/hIUXuThuKmRfna8G3kBTxuxWPZRoHTwPjTqwcxWb9lWvgEo6UtUHH9fjaxgrBoDHf+UN9t5h95KXSObKb7ifj2F0eLiJgZqeTt4dM8+ohyS++C+bXXAzIH4R7RS3Xg4NcSBwiJl49vhtu066lcIfpo6yd4ZVD5LkhNk+chCBNOdPRGyW4MJrOFU3vp+o4LUI2QB/rfEEGqmEPrMiA/oa5/vuy8NuPAGDQ2aEpKJH0KtLFhs0Rzg+x3eTMzsAfF+mdsC5aRpzyXObMpbL73KXlsWAqQ7mGE3YkvE9GHtX6qc6st4W4pXViLMe9xtZl0xDPEKXKF4+SjZUjlBPzhWHeWqFAHdvq/HetHMo3lwvlVktnwUOhlV4iNqY0EJJpsEnb6dEhjdKa7+mqFZfOY2thHxDT7hJYO+OIE+z/48b+w4NhOi7dc3G8yNcTcUGAk7ZWO23uFs1kzMtMgOmJUJ+AHEwlnn6JDj3eHVlODy718zoY1ipTiyqxTGAk8O57zyF+4az5ciinzyWBVx3UpOEzOppJ9elQGz+stVj4iOsWLnyD25xb1UAl10pMPP4Ttu3IzViIbZRr+Vib/ZxjMwHM4zNugUUmEWT7R9d570cb50RG5sJzBIUm0+ak+k87AA2l8KX67EiO8TxwICTIxu74E6oUunRcxSxFzQ8d4v2lnO

grep rcon server.properties

$env:SPOTIPY\_CLIENT\_ID="ec69ef77b7424726bc56714e5d7bcc6b"  
$env:SPOTIPY\_CLIENT\_SECRET="10ad06b837c641309bf8bb5af2852993"

$env:SPOTIPY\_CLIENT\_ID="ec69ef77b7424726bc56714e5d7bcc6b"  
$env:SPOTIPY\_CLIENT\_SECRET="10ad06b837c641309bf8bb5af2852993"  
