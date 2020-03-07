import React from 'react';

class diet extends React.Component{
    render(){
        if (this.props.currentStep !== 2) {
            return null
          } 
          return(
            <div className="form-group">
              <label htmlFor="username">Diet</label>
              <input
                id="diet"
                name="diet"
                type="text"
                placeholder="Enter diet"
                value={this.props.diet}
                onChange={this.props.handleChange}
                />
            </div>
          );
        
    }
}
export default diet;