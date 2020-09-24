import React, { Component }  from "react";
import Button from './component/button';
import './css/style.css';
import 'bootstrap/dist/css/bootstrap.css';


class App extends Component{
  constructor(props){
    super (props);


    this.state = {
      Current: '0',
      vorigen: [],
      nextIsrest: false
    }
  }


  reset = () => {
    this.setState({Current: '0', vorigen: [], nextIsrest: false});

  
  }
  addToCurrent = (symbol) => {
    if(["/","-","+","*"].indexOf(symbol) > -1){
      let {vorigen} = this.state;
      vorigen.push(this.state.Current + symbol);
      this.setState({vorigen, nextIsrest: true});
    }else{  
      if((this.state.Current === "0" && symbol !==".") || this.state.nextIsrest){
      this.setState({Current: symbol, nextIsrest: false});
      }else{
        this.setState({Current: this.state.Current + symbol});
      }
    }
  }
  rekenen = (symbol) => {
    let {Current, vorigen, nextIsrest} = this.state;
    if(vorigen.length > 0 ){
      Current = eval(String(vorigen[vorigen.length -1] + Current));
      this.setState({Current, vorigen: [],nextIsrest: true});
    }
  }
render() {
  const buttons = [
    {symbol: 'c', cols:3, action: this.reset},
    {symbol: '/', cols:1, action: this.addToCurrent},
    {symbol: '7', cols:1, action: this.addToCurrent},
    {symbol: '8', cols:1, action: this.addToCurrent},
    {symbol: '9', cols:1, action: this.addToCurrent},
    {symbol: '*', cols:1, action: this.addToCurrent},
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
    {symbol: '=', cols:1, action: this.rekenen},




  ];
    return(
      <div  classname="App"> 
        {this.state.vorigen.length > 0 ?
        <div class="floaty-last">{this.state.vorigen[this.state.vorigen.length - 1]}</div>
        :null}
        <input className = 'resultaat' type="text" value={this.state.Current} />
        <div classname = "row">
          <div classname = "container">
            {buttons.map((btn, i) => {
              return <Button key={i} symbol={btn.symbol} cols={btn.cols}  action={(symbol) => btn.action(symbol)} />
            })}
          </div>
        </div>



      </div>
    );
  }

}
export default App;