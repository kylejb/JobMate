import Form from 'components/Form';
import Navbar from 'components/Navbar';
function App() {
	return (
		<div className='app'>
			<Navbar />
			<h1>App Component</h1>
			<Form exampleProp='typeString' />
		</div>
	);
}

export default App;
