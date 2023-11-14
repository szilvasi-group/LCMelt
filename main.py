import streamlit as st
import pandas as pd
import numpy as np


st.header("LCMelt v1.1: A Liquid Crystal Melting Point Prediction App")
st.text_input("Enter a valid SMILES string for your molecule: ", key="SMILES")

if st.button('Make prediction'):
    import chemprop

    smiles = [[st.session_state.SMILES]]
    arguments = [
        '--test_path', '/dev/null',
        '--preds_path', '/dev/null',
        '--checkpoint_dir', 'Model/'
    ]

    args = chemprop.args.PredictArgs().parse_args(arguments)
    preds = chemprop.train.make_predictions(args=args, smiles=smiles)
    st.write(f"The melting point of your molecule is: {int(np.squeeze(preds)) - 10} degrees Celsius")
