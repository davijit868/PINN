<p align='center' style = "font-size: 20px; font-family: 'Open Sans', verdana, arial, sans-serif;"> Visualizing Learning of Domain-Specific Knowledge in Neural Networks</p>

<p style = "font-size : 12px; font-family: 'Open Sans', verdana, arial, sans-serif; ">This visualizer displays how the neural networks has learnt the physics laws that govern the observed data when it is not explicitly enforced and when it is explicitly enforced. Burgers’ Equation (du/dt + u.du/dx – (0.01/π).d<sup>2</sup>u/dx<sup>2</sup> = 0) is the fundamental partial differential equation for this demo use case. The accuracy of neural network predictions are typically represented as error (|u<sub>Predicted</sub> – u<sub>Observed Data</sub>|) and rendered as plot series (u<sub>Observed Data</sub> vs t, u<sub>Predicted</sub> vs t) as seen in u<sup>error</sup> bar plot and u vs t line plot. While u is a representation of the conformance of the model with respect to the PDE, it is not a direct measure of the same. Our Visualizer observes and renders the learning of domain-specific knowledge (PDE) in neural networks more precisely. The learning of Burgers’ equation in neural networks is represented by two series for given x: Series with du/dt vs t and Series with u.du/dx - (0.01/π).d<sup>2</sup>u/dx<sup>2</sup> vs t. The area between these two series represents the non-conformance of model with the Burgers’ equation.</p>
 
 Author: Kamalkumar Rathinasamy
 
