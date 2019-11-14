import React, { Component } from "react";
import PropTypes from "prop-types";

class NoteViewer extends Component {
  render() {
    const { note } = this.props;
    return (
      <div>
        <textarea disabled>{note.title}</textarea>
        <textarea disabled>{note.content}</textarea>
      </div>
    );
  }
}

NoteViewer.propTypes = {
  note: PropTypes.shape({
    id: PropTypes.number,
    title: PropTypes.string,
    content: PropTypes.string
  }).isRequired
};

export default NoteViewer;
