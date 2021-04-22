import React from 'react';
import styled from 'styled-components';

const Title = styled.h1`
	font-size: 1.5em;
	text-align: center;
	color: palevioletred;
`;
const Wrapper = styled.section`
	padding: 4em;
	background: papayawhip;
`;

function Navbar() {
	return (
		<div>
			<Wrapper>
				<Title>Hello</Title>
			</Wrapper>
		</div>
	);
}

export default Navbar;
