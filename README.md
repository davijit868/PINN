<p align='center' style = "font-size: 20px; font-family: 'Open Sans', verdana, arial, sans-serif;"> <b>Visualizing Learning of Domain-Specific Knowledge in Neural Networks</b></p>
<p> <b> Authors: </b> <b> Kamalkumar Rathinasamy </b> (Infosys; https://twitter.com/kamlkumr, https://www.linkedin.com/in/kaml/), <b> Avijit Das </b> (Infosys; https://www.linkedin.com/in/davijit868/) & <b> Soundararajan Rajendran </b> (RKM Vivekananda College; soundararajan.rajendran@gmail.com).</p>
<p> <b> Presenter: </b> Kamalkumar Rathinasamy. </p>
<p> <b> Context: </b> Machine learning systems are heavily dependent on quality & quantity of training data, complex neural network structures and extensive computational effort. Since they often fail to converge in data-limited domains, it is necessary for machine learning systems to learn in a sample-efficient manner. Leveraging domain-specific knowledge can act as a regularization agent to constrain the space of acceptable machine learning solutions. Physics Informed Neural Networks are neural networks that are trained to solve supervised learning tasks while honoring any given physics law described by PDEs. Our visualizer displays how the neural networks has learnt the physics laws that govern the observed data when it is not explicitly enforced and when it is explicitly enforced.</p>
<p> <b> Description: </b> Burgers’ Equation (du/dt + u.du/dx – (0.01/π).d<sup>2</sup>u/dx<sup>2</sup> = 0) is the fundamental partial differential equation for this demo use case. The accuracy of neural network predictions are typically represented as error (|u<sub>Predicted</sub> – u<sub>Observed Data</sub>|) and rendered as plot series (u<sub>Observed Data</sub> vs t, u<sub>Predicted</sub> vs t) as seen in u<sup>error</sup> bar plot and u vs t line plot. While u is a representation of the conformance of the model with respect to the PDE, it is not a direct measure of the same. Our Visualizer observes and renders the learning of domain-specific knowledge (PDE) in neural networks more precisely. The learning of Burgers’ equation in neural networks is represented by two series for given x: Series with du/dt vs t and Series with u.du/dx - (0.01/π).d<sup>2</sup>u/dx<sup>2</sup> vs t. The area between these two series represents the non-conformance of model with the Burgers’ equation.</p>
<p> <b> Code: </b> https://github.com/davijit868/PINN/tree/master/code </p>
<p> <b> Results, Outcomes, Conclusions: </b> It is observed that the nonconformity to fundamental physics law impacts the model performance. </p>
<p> <b> Python Libraries Used: </b> TensorFlow, Plotly. </p>
<p> <b> Open Questions/Issues : </b>  In this work, the error in prediction and the error in non-conformity to physics law, are compared and studied. Are there more to be observed from the results than just comparing the errors? </p>
