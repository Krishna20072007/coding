function setup() {
    createCanvas(400, 400);
    background(0, 225, 255);
    angleMode(DEGREES);
    translate(width / 2, height / 2);
    fill(0, 255, 0);
    noStroke();
    arc(
      0,
      (1 * height) / 2,
      -1 * width - width / 12,
      height - height / 4,
      180,
      -180
    );
    
    // Cloud
    fill(255);
    makeCloud(random(-75, -125), random(-140, -160));
    makeCloud(random(75, 125), random(-130, -150));
  
    // Tree
    fill(0, 255, 0);
    
    
    makeTree(random(115, 135), random(190, 210))
    makeTree(random(470, 490), random(380, 400))
  }
  
  function makeCloud(cloudx, cloudy) {
    noStroke();
    ellipse(cloudx, cloudy, 70, 50);
    ellipse(cloudx + 20, cloudy + 10, 70, 50);
    ellipse(cloudx - 20, cloudy + 10, 70, 50);
  }
  
  function makeTree(treex, treey) {
    strokeWeight(5);
    translate(-width / 2, -height / 2);
    stroke(101, 67, 33);
    fill(102, 51, 0);
    line(treex -35, treey, treex -35, treey +75);
    line(treex, treey, treex, treey +75);
    fill(0, 255, 0);
    makeCloud(treex -35 / 2, treey -75 / 3);
  }
  