import React from 'react';

class name extends React.Component {
    render(){
        if (this.props.currentStep !== 1) {
            return null
          } 
          return(
            <div className="inputs">
              <label htmlFor="name">Name</label>
              <input
                id="name"
                name="name"
                type="text"
                placeholder="Enter Name"
                value={this.props.name}
                onChange={this.props.handleChange}
                />
            </div>
          );
    }
  }

export default name;