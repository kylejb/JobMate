import Button from 'components/Button';

interface FormProp {
  exampleProp: String;
}

const Form = (props: FormProp) => {
  return (
    <div>
      <h1>Nice Form</h1>
      <Button />
    </div>
  );
}

export default Form;
