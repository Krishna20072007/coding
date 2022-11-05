function draw() {
  for (let i = 0; i < 10; i++) {
    angleMode(DEGREES)
    frameRate(2)
    createCanvas(400, 400);
    noFill();
    background(252, random(198, 252), 3);
    translate(width/2, height/2);
    strokeWeight(random(5, 12));
    smooth();

    let eye =  random(50, 100)

      ellipse(-75, -50, 50, eye);
    ellipse(75, -50, 50, eye);
    arc(0, 50, 300, 200, 360, 180);

    // saveCanvas("smile.jpg");
  }
}
