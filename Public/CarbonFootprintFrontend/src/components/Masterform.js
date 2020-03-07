import React from 'react';
import Transportation from './Steps/transportation';
import Diet from './Steps/diet';
import Name from './Steps/name';
class Masterform extends React.Component {
    constructor(props) {
      super(props)
      this.state = {
        currentStep: 1,
        name:  '',
        transportation: '',
        diet: '', 
      }
    }
  
    handleChange = event => {
      const {name, value} = event.target
      this.setState({
        [name]: value
      })    
    }
     
    handleSubmit = event => {
      event.preventDefault()
      const { name, diet, transportation } = this.state
      alert(`Your registration detail: \n 
             Name: ${name} \n 
             Diet: ${diet} \n
             Transportation: ${transportation}`)
    }
    
    _next = () => {
      let currentStep = this.state.currentStep
      currentStep = currentStep >= 2? 3: currentStep + 1
      this.setState({
        currentStep: currentStep
      })
    }
      
    _prev = () => {
      let currentStep = this.state.currentStep
      currentStep = currentStep <= 1? 1: currentStep - 1
      this.setState({
        currentStep: currentStep
      })
    }
  
  /*
  * the functions for our button
  */
  previousButton() {
    let currentStep = this.state.currentStep;
    if(currentStep !==1){
      return (
        <button 
          type="button" onClick={this._prev}>
        Previous
        </button>
      )
    }
    return null;
  }
  
  nextButton(){
    let currentStep = this.state.currentStep;
    if(currentStep <3){
      return (
        <button 
          type="button" onClick={this._next}>
        Next
        </button>        
      )
    }
    return null;
  }
    
    render() {    
      return (
        <div>
        <h1 className="form-title">Carbon Footprint Calculator</h1>
        <p>Step {this.state.currentStep} </p> 
  
        <form onSubmit={this.handleSubmit}>
        {/* 
          render the form steps and pass required props in
        */}
          <Name 
            currentStep={this.state.currentStep} 
            handleChange={this.handleChange}
            name={this.state.name}
          />
          <Diet 
            currentStep={this.state.currentStep} 
            handleChange={this.handleChange}
            diet={this.state.diet}
          />
          <Transportation 
            currentStep={this.state.currentStep} 
            handleChange={this.handleChange}
            transportation={this.state.transportation}
          />
          {this.previousButton()}
          {this.nextButton()}
  
        </form>
        </div>
      );
    }
  }

export default Masterform;