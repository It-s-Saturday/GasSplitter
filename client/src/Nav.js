import Container from 'react-bootstrap/Container';
import Navbar from 'react-bootstrap/Navbar';
import React from 'react';

export default function Nav() {
    return (
        <Navbar bg="light">
        <Container>
          <Navbar.Brand href="#home">Gas Splitter</Navbar.Brand>
        </Container>
      </Navbar>
    )
}