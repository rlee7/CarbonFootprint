import React from 'react';

class transportation extends React.Component {
    render(){
        if (this.props.currentStep !== 3) {
            return null
          } 
          return(
            <div>
            <div className="inputs">
              <label htmlFor="transportation">Method of Transportation</label>
              <input
                id="transportation"
                name="transportation"
                type="transportation"
                placeholder="Enter transportation types"
                value={this.props.transportation}
                onChange={this.props.handleChange}
                />      
            </div>
            <button className="enter-button">Enter</button>
            </div>
          );
    }
}

export default transportation;