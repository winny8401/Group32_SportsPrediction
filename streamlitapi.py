import pickle
import streamlit as st

import joblib

# Load the model using joblib
model = joblib.load('C:/Users/berni/OneDrive\Desktop/projectmidsem/FIFA_football_prediction_model.pkl')


def main():
    st.title('FIFA Player Rating Prediction')

    # Input variables
    age = st.number_input('Player Age', min_value=16, max_value=45)
    movement_reactions = st.number_input('Movement Reactions', min_value=0, max_value=100)
    mentality_composure = st.number_input('Mentality Composure', min_value=0, max_value=100)
    passing = st.number_input('Passing', min_value=0, max_value=100)
    potential = st.number_input('Potential', min_value=0, max_value=100)
    release_clause_eur = st.number_input('Release Clause (EUR)')
    dribbling = st.number_input('Dribbling', min_value=0, max_value=100)
    wage_eur = st.number_input('Wage (EUR)')
    power_shot_power = st.number_input('Power Shot Power', min_value=0, max_value=100)
    value_eur = st.number_input('Value (EUR)')
    mentality_vision = st.number_input('Mentality Vision', min_value=0, max_value=100)
    attacking_short_passing = st.number_input('Attacking Short Passing', min_value=0, max_value=100)
    physic = st.number_input('Physic', min_value=0, max_value=100)
    skill_long_passing = st.number_input('Skill Long Passing', min_value=0, max_value=100)
    goals_scored = st.number_input('Goals Scored', min_value=0, max_value=100)
    shooting = st.number_input('Shooting', min_value=0, max_value=100)
    skill_ball_control = st.number_input('Skill Ball Control', min_value=0, max_value=100)
    international_reputation = st.number_input('International Reputation', min_value=0, max_value=5)
    skill_curve = st.number_input('Skill Curve', min_value=0, max_value=100)
    attacking_crossing = st.number_input('Attacking Crossing', min_value=0, max_value=100)

    #  prediction code 
    if st.button('Predict Player Rating'):
       
        input_data = [movement_reactions, mentality_composure, passing, potential, release_clause_eur,
                      dribbling, wage_eur, power_shot_power, value_eur, mentality_vision, attacking_short_passing,
                      physic, skill_long_passing, age, shooting, skill_ball_control, international_reputation,
                      skill_curve, attacking_crossing,goals_scored]
        predicted_rating = model.predict([input_data])
        st.write(f'Predicted Player Rating: {predicted_rating[0]}')

if __name__ == '__main__':
    main()
