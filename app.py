from flask import Flask

app = Flask(__name__)

HTML = r"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Snake</title>
<style>
  body{background:#111;color:#eee;font-family:sans-serif;text-align:center}
  canvas{background:#000;border:2px solid #4caf50}
</style>
</head>
<body>
<h2>Snake 🐍</h2>
<p>Score: <span id="s">0</span></p>
<canvas id="c" width="400" height="400"></canvas>
<script>
const c=document.getElementById('c'), x=c.getContext('2d'), G=20, N=20;
let snake, dir, food, score, loop;

function start(){
  snake=[{x:10,y:10}]; dir={x:1,y:0}; score=0;
  document.getElementById('s').textContent=score;
  place(); clearInterval(loop); loop=setInterval(tick,120);
}
function place(){
  food={x:Math.floor(Math.random()*N), y:Math.floor(Math.random()*N)};
}
function tick(){
  const h={x:snake[0].x+dir.x, y:snake[0].y+dir.y};
  if(h.x<0||h.y<0||h.x>=N||h.y>=N||snake.some(p=>p.x==h.x&&p.y==h.y)){start();return;}
  snake.unshift(h);
  if(h.x==food.x&&h.y==food.y){score++;document.getElementById('s').textContent=score;place();}
  else snake.pop();
  x.fillStyle='#000'; x.fillRect(0,0,400,400);
  x.fillStyle='red'; x.fillRect(food.x*G,food.y*G,G-2,G-2);
  x.fillStyle='lime'; snake.forEach(p=>x.fillRect(p.x*G,p.y*G,G-2,G-2));
}
document.addEventListener('keydown',e=>{
  const k=e.key;
  if(k=='ArrowUp'&&dir.y==0)dir={x:0,y:-1};
  if(k=='ArrowDown'&&dir.y==0)dir={x:0,y:1};
  if(k=='ArrowLeft'&&dir.x==0)dir={x:-1,y:0};
  if(k=='ArrowRight'&&dir.x==0)dir={x:1,y:0};
});
start();
</script>
</body>
</html>"""

@app.route("/")
def home():
    return HTML

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
