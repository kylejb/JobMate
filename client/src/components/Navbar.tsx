import styled from 'styled-components';
import { BrowserRouter, NavLink } from 'react-router-dom';

const Title = styled.div`
	font-size: 1.5em;
	color: #fffffe;
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
			<Nav>
				<BrowserRouter>
					<Title>JobMate</Title>
					<StyledLink
						className='nav-link'
						activeClassName='is-active'
						exact={true}
						to='/about'
					>
						About us
					</StyledLink>
				</BrowserRouter>
			</Nav>
		</div>
	);
}

export default Navbar;
