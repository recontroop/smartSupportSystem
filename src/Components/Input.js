import React from 'react';
import { Button } from 'react-bootstrap';
import { Grid } from 'react-bootstrap';
import { Col } from 'react-bootstrap';
import { Row } from 'react-bootstrap';
import { Navbar } from 'react-bootstrap';
import { FormControl } from 'react-bootstrap';

class Input extends React.Component {


        constructor(props) {
            super(props);

            this.state = {  
                description: ''
            };

            this.handleSubmit = this.handleSubmit.bind(this);
            this.handleChange = this.handleChange.bind(this);
        }

        handleChange = (e)  =>{
            this.setState({ description: e.target.value });
        }

        handleSubmit(event) {
            event.preventDefault();

            const { description } = this.state.description;
            
            fetch('http://172.22.205.141:8000/customerQuery', {
                method: 'POST',
                body: JSON.stringify({description: this.state.description })
            })
            .then( (response) => {
                alert(response)
            });
        }

    render() {
        return ( 
            <div>

                <Navbar>
                    <Navbar.Header>
                        <Navbar.Brand>
                            {/* <img width={15} height={15} src="upslogo.png" alt="UPS logo" /> */}
                            <img width={50} height={70} src={require('./upslogo.png')} />
                        </Navbar.Brand>
                        <Navbar.Toggle />
                    </Navbar.Header>
                    <Navbar.Collapse>
                        <Navbar.Text>
                            
                        </Navbar.Text>
                        <Navbar.Text pullRight>SSS - Smart Solution System</Navbar.Text>
                    </Navbar.Collapse>
                </Navbar>

                <br />
                <br />

                <h2>Provide the information below</h2>

                <br />
                <br />

                <form  onSubmit={this.handleSubmit}>
                    <Grid>
                        <Row className="show-grid">
                            <Col xs={12} md={6}>
                                <FormControl type="text" placeholder="Full Name" />
                            </Col>
                            <Col xs={12} md={6}>
                             <FormControl type="text" placeholder="Phone Number" />
                            </Col>
                        </Row>

                        <br />

                        <Row className="show-grid">
                            <Col xs={12} md={12}>
                                <FormControl type="text" placeholder="Tracking Number" />
                            </Col>
                            
                        </Row>

                        <br />

                        <Row className="show-grid">
                            <Col xs={12} md={12}>
                                <FormControl componentClass="textarea" placeholder="Enter Problem" onChange={this.handleChange}/>
                            </Col>
                        </Row>

                        <br />

                        <Row className="show-grid">
                            <Col xs={12} md={12}>
                             <Button bsStyle="primary" type = "submit" value = "Submit" > Submit </Button> 
                            </Col>
                        </Row>

                    </Grid>
                </form> 

            </div>
        );
    }
}

export default Input;

