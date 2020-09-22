import React, { Component }  from 'react';


class Aplication extends Component{
constructor(props){
    super (props);
    this.state = {
        count: 0,
        overTen:  false

    }
}
hendelClick = () => {
this.setState({count: this.state.count + 1})
}

componentDidUpdate(props,state){
if(this.state.count  > 10 && this.state.count !== state.count){
    this.setState({overTen: true});
}

}


render(){
    let {count} = this.state;

   
        return (
            <div>
                <h1>je hebt op de button {count} geklikt</h1>
                {(this.state.overTen)? 
                <h3>verslaa de high scoore van 10</h3>
                :null
                
            }
                <span>
                    <button onClick={(e) => this.hendelClick()}> druk me </button>
                </span>
            </div>
        )
            
                
        }
}
export default Aplication;