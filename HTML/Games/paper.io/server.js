const MiServer = require("mimi-server");
const express = require("express");
const path = require("path");
const { exec, fork } = require("child_process");

const config = require("./config.json");
config.dev ? exec("npm run build-dev") : exec("npm run build");

const port = process.env.PORT || config.port;

const { app, server } = new MiServer({
  port,
  static: path.join(__dirname, "public"),
});

const io = require("socket.io")(server);

// Routing
app.use(
  "/font",
  express.static(
    path.join(__dirname, "node_modules/@fortawesome/fontawesome-free")
  )
);

const Game = require("./src/game-server");
const game = new Game();

io.on("connection", (socket) => {
  socket.on("hello", (data, fn) => {
    //TODO: error checking.
    if (data.god && game.addGod(socket)) {
      fn(true);
      return;
    }
    if (data.name && data.name.length > 32) fn(false, "Your name is too long!");
    else if (!game.addPlayer(socket, data.name))
      fn(false, "There're too many players!");
    else fn(true);
  });
  socket.on("pings", (fn) => {
    socket.emit("pongs");
    socket.disconnect();
  });
});

setInterval(() => {
  game.tickFrame();
}, 1000 / 60);

for (let i = 0; i < parseInt(config.bots); i++) {
  fork(path.join(__dirname, "paper-io-bot.js"), [`ws://localhost:${port}`], {
    stdio: "inherit",
  });
}
