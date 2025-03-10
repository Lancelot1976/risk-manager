import React from 'react';
import logo from './logo.svg';
import './App.css';
import GuiList from './Gui/GuiList';

const data=[
  {'id':1,'risk':'Risk1'},
  {'id':2,'risk':'Risk2'},
  {'id':3,'risk':'Risk3'},
  {'id':4,'risk':'Risk4'},
  {'id':5,'risk':'Risk5'},
  {'id':6,'risk':'Risk6'},
  {'id':7,'risk':'Risk7'},
  {'id':8,'risk':'Risk8'},
  {'id':9,'risk':'Risk9'},
  {'id':10,'risk':'Risk10'},
]

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <GuiList data={data}/>
      </header>
    </div>
  );
}

export default App;
