const express = require('express');


const PORT = process.env.PORT || 3000;
const app = express();

app.get('/', (req, res) => {
  res.send("<h1>Hello there</h1>")
});

app.listen(PORT, () => {
  console.log(`Started listening on port ${PORT}`);
});
