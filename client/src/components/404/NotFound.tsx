import styled from 'styled-components';

const ErrorTitle = styled.p`
    font-size: 6em;
    color: red;
`;
const ErrorContent = styled.p`
    font-size: 1em;
`;
const ErrorMsg = styled.div`
    margin: 1em;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
`;
export default function NotFound() {
    return (
        <ErrorMsg>
            <ErrorTitle>Error!</ErrorTitle>
            <ErrorContent>
                The page you are looking for does not exist.
            </ErrorContent>
            <ErrorContent>
                Please click the top left to go back to the home page.
            </ErrorContent>
        </ErrorMsg>
    );
}
