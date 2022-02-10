<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta http-equiv="X-UA-Compatible" content="ie=edge" />
    <title>Calculator</title>
    <link
      rel="stylesheet"
      href="https://cdnjs.cloudflare.com/ajax/libs/skeleton/2.0.4/skeleton.min.css"
    />

    <style>
      .alert {
        background: green;
        padding: 1rem;
        border-radius: 5px;
        color: white;
        margin: 1rem;
      }
    </style>
  </head>
  <body>
    <div class="container">
      <h3>Calculator App</h3>
    </div>

    <!-- Form -->
    <div class="container">
      <form action="/send" method="POST">
        <label for="Number One">First Number</label>
        <input
          type="text"
          placeholder="First Number"
          class="u-full-width"
          name="num1"
        />

        <label for="Number Two">Second Number</label>
        <input
          type="text"
          placeholder="Second Number"
          class="u-full-width"
          name="num2"
        />

        <label for="Operation">Operation</label>
        <select class="u-full-width" name="operation">
          <option value="add">Add</option>
          <option value="subtract">Subtract</option>
          <option value="multiply">Multiply</option>
          <option value="divide">Divide</option>
        </select>

        <input type="submit" value="Calculate" id="calc_btn" />
        <br />
<div id="outputDiv" style="width: 500px; height: 75px; border: 1px solid;"> {{sum}}</div>
        </div>
      </form>
    </div>
  </body>
</html>
