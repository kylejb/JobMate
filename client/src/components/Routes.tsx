import { Switch, Route } from 'react-router-dom';
import NotFound from 'components/404';
import About from 'components/About';
import Homepage from 'components/Homepage';
export default function Routes() {
	return (
		<Switch>
			{/* Private Routes */}
			{/* <PrivateRoute exact path='/dashboard' component={Dashboard}} */}
			<Route exact path='/' component={Homepage}></Route>
			<Route path='/about' component={About}></Route>
			<Route component={NotFound}></Route>
		</Switch>
	);
}
