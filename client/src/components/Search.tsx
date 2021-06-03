import { ChangeEvent, useState } from 'react';
import styled from 'styled-components';

const SearchContainer = styled.div`
    margin: 3em;
    display: flex;
    justify-content: center;
    align-items: center;
`;
const SearchBar = styled.input`
    margin: 1em;
    border: 1px solid grey;
    border-radius: 5px;
    height: 50px;
    width: 100%;
    padding: 2px 23px 2px 30px;
    outline: 0;
    background-color: #f5f5f5;
    &:hover,
    &:focus {
        border: 1.5px solid #094067;
        background-color: white;
    }
`;
const SearchButton = styled.button`
    background-color: #094067;
    border: none;
    color: white;
    border-radius: 5px;
    padding: 17px 32px;

    &:hover {
        background-color: #ef4565;
        transform: translateY(-100px);
    }
    &:active {
        transform: translateY(100px);
    }
`;
function Search() {
    const [searchValue, setSearchValue] = useState('');

    const changeHandler = (e: ChangeEvent<HTMLInputElement>) => {
        setSearchValue(e.target.value);
    };
    const submitHandler = async () => {
        const url =
            searchValue.length === 0
                ? `http://localhost:8000/listings/`
                : `http://localhost:8000/listings/?search=${searchValue}`;
        const res = await fetch(url);
        let data = await res.json();
        console.log(data);
    };
    return (
        <SearchContainer>
            <SearchBar
                type="search"
                value={searchValue}
                placeholder="Search..."
                onChange={changeHandler}
            ></SearchBar>
            <SearchButton type="button" onClick={submitHandler}>
                Search
            </SearchButton>
        </SearchContainer>
    );
}

export default Search;
