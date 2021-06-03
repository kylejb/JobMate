import styled from 'styled-components';
import { BrowserRouter as Router, NavLink } from 'react-router-dom';
import AllRoutes from 'components/Routes';

const Title = styled(NavLink)`
	font-size: 1.5em;
	color: #fffffe;
	text-decoration: none;
`;
const Nav = styled.nav`
	padding: 0.5em;
	background: #094067;
	display: flex;
	justify-content: space-between;
`;

const StyledLink = styled(NavLink)`
	display: block;
	color: #ef4565;
	font-weight: bold;
	text-decoration: none;
	&:hover {
		background: white;
		color: black;
	}
`;

function Navbar() {
	return (
		<div>
			<Router>
				<Nav>
					<Title
						className='nav-link'
						activeClassName='is-active'
						exact={true}
						to='/'
					>
						JobMate
					</Title>
					<StyledLink
						className='nav-link'
						activeClassName='is-active'
						exact={true}
						to='/about'
					>
						About us
					</StyledLink>
				</Nav>
				<AllRoutes />
			</Router>
		</div>
	);
}

export default Navbar;
