import React from 'react';

class Header extends React.Component {

    constructor(props) {
        super(props)
        this.state = {}
    }

    componentDidMount() {
        fetch("http://172.22.205.141:8000/test")
            .then(res => res.json())
            .then(res => {
                this.setState({
                    testData: res
                })
            })
    }

    render() {

        if(!this.state.testData) return <p> Loading.... </p>
        return ( 
            <div>
            {this.state.testData.message}
            </div>
        );
    }
}

export default Header;