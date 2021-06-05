import React from 'react';

class Timer extends React.Component {
    constructor (props) {
        super(props);
        this.state = {
            seconds: 0
        };
    }

    tick() {
        this.setState(state => ({
            seconds: state.seconds + 1 
        }))
    }

    // This function will be called once the state has been updated and mounting
    componentDidMount() {
        this.interval = setInterval(() => this.tick(), 1000);
    }

    // Called immediately before a component is destroyed. 
    // Perform any necessary cleanup in this method, such as cancelled network 
    // requests, or cleaning up any DOM elements created in componentDidMount.
    componentWillUnmount() {
        clearInterval(this.interval);
    }

    // What actually gets rendered as a component
    render() {
        return (
            <div>
                Seconds: {this.state.seconds}
            </div>
        )
    }
}

export default Timer;