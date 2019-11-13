import React, { Component } from "react";
import PropTypes from "prop-types";

const NotePicker = props => (
  <div>
    {props.notes.map(note => (
      <li key={note.id}>{note.title}</li>
    ))}
  </div>
);

NotePicker.propTypes = {
  notes: PropTypes.arrayOf(
    PropTypes.shape({
      id: PropTypes.number,
      title: PropTypes.string,
      content: PropTypes.string
    })
  ).isRequired
};

export default NotePicker;
