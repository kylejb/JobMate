import React from 'react';
import styled from 'styled-components';
const AboutContainer = styled.div`
    display: flex;
    margin: 5em;
    justify-content: center;
    align-items: center;
`;
const AboutTitle = styled.p`
    font-size: 60px;
`;
const AboutContent = styled.p`
    font-size: 0.5em;
`;
export default function About() {
    return (
        <AboutContainer>
            <AboutTitle>
                About us
                <AboutContent>
                    Lorem Ipsum is simply dummy text of the printing and
                    typesetting industry. Lorem Ipsum has been the industry's
                    standard dummy text ever since the 1500s, when an unknown
                    printer took a galley of type and scrambled it to make a
                    type specimen book. It has survived not only five centuries,
                    but also the leap into electronic typesetting, remaining
                    essentially unchanged. It was popularised in the 1960s with
                    the release of Letraset sheets containing Lorem Ipsum
                    passages, and more recently with desktop publishing software
                    like Aldus PageMaker including versions of Lorem Ipsum.
                </AboutContent>
            </AboutTitle>
        </AboutContainer>
    );
}
