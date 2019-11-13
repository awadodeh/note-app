import React, { Component } from "react";
import styled from "styled-components";
import NoteViewer from "components/NoteViewer";
import NotePicker from "components/NotePicker";
import api from "api";

class App extends Component {
  state = { notes: [], selectedNote: null };

  componentDidMount() {
    api.get("/notes").then(response => {
      const notes = response.data;
      const selectedNote = notes.length > 0 ? 0 : null;
      this.setState({ notes, selectedNote });
    });
  }
  render() {
    const { notes, selectedNote } = this.state;

    return (
      <Container>
        <NotePicker notes={notes} />
        {selectedNote !== null && <NoteViewer note={notes[selectedNote]} />}
      </Container>
    );
  }
}

export default App;

const Container = styled.div`
  display: flex;
  flex-direction: row;
  & > * {
    margin: 10px;
    padding: 0px;
  }
  & > * > * {
    margin: 5px;
    padding: 0px;
  }

  & > * > textarea {
    width: 200px;
    height: 150px;
  }
`;
