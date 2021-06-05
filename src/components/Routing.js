import React from 'react';
import { Link, Route, Switch } from "react-router-dom";
import { BrowserRouter as Router } from "react-router-dom";
const Home = () => (
    <h2>This is the Home page</h2>
)

const About = () => (
    <h2>This is an About page</h2>
)

const Contract = () => (
    <h2>This is Contract Page</h2>
)

const Products = () => (
    <h2>This is Products Page</h2>
)


export default function Routing() {
    return (
    < Router >
            <div>
                <nav>
                    <ul>
                        <li>
                            <Link to="/">Home</Link>
                        </li>
                        <li>
                            <Link to="/about">About</Link>
                        </li>
                        <li>
                            <Link to="/contract">Contract</Link>
                        </li>
                        <li>
                            <Link to="/products">Products</Link>
                        </li>
                    </ul>
                </nav>

                {/* When the current url matches any of the path property, following will rendered */}
                <Switch>
                    <Route path="/about">
                        <About/>
                    </Route>
                    <Route path="/contract">
                        <Contract/>
                    </Route>
                    <Route path="/products">
                        <Products/>
                    </Route>
                    <Route path="/">
                        <Home/>
                    </Route>
                </Switch>
            </div>
    </ Router>
    );
}