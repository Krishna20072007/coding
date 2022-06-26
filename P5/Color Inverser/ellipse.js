class circ {
  constructor(x, y, r) {
    this.x = x;
    this.y = y;
    this.r = r;
  }

  show() {
    fill(255 - r, 255 - g, 255 - b);
    noStroke();
    ellipse(this.x, this.y, this.r);
  }

  move() {
    this.x = this.x + random(this.y);
    this.y = this.y + random(this.x);
  }

  restrict() {
    if (this.x <= 0 || this.x > width) {
      this.x = width / 2;
    }

    if (this.y < 0 || this.y > height) {
      this.y = height / 2;
    }
  }
}
