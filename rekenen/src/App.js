import React, { Component }  from "react";
import Button from './component/button';
import './css/style.css';


class App extends Component{
  constructor(props){
    super (props);


    this.state = {
      Current: '0',
      vorigen: []
    }
  }


  reset = () => {
    this.setState({reset: 0});

  
  }
  addToCurrent = (symbol) => {
    this.setState({Current: this.state.Current+ symbol});
  }
render() {
  const buttons = [
    {symbol: 'c', cols:3, action: this.reset},
    {symbol: '/', cols:1, action: this.addToCurrent},
    {symbol: '7', cols:1, action: this.addToCurrent},
    {symbol: '8', cols:1, action: this.addToCurrent},
    {symbol: '9', cols:1, action: this.addToCurrent},
    {symbol: 'x', cols:1, action: this.addToCurrent},
    {symbol: "4", cols:1, action: this.addToCurrent},
    {symbol: '5', cols:1, action: this.addToCurrent},
    {symbol: '6', cols:1, action: this.addToCurrent},
    {symbol: '-', cols:1, action: this.addToCurrent},
    {symbol: '3', cols:1, action: this.addToCurrent},
    {symbol: '2', cols:1, action: this.addToCurrent},
    {symbol: '1', cols:1, action: this.addToCurrent},
    {symbol: '+', cols:1, action: this.addToCurrent},
    {symbol: '0', cols:2, action: this.addToCurrent},
    {symbol: '.', cols:1, action: this.addToCurrent},
    {symbol: '=', cols:1, action: this.addToCurrent},




  ];
    return(
      <div  classname="App">
        <input className = 'resultaat' type="text" value={this.state.Current} />
        {buttons.map((btn, i) => {
          return <Button key={i} symbol={btn.symbol} cols={btn.cols}  action={(symbol) => btn.action(symbol)} />
        })}



      </div>
    );
  }

}
export default App;