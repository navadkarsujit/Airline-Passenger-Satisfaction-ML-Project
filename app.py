import pickle
import streamlit as st
import numpy as np

pickle_sc=open('scaling.pkl', 'rb')
scaling=pickle.load(pickle_sc)

pickle_in=open('LRmodel.pkl', 'rb')
LRmodel=pickle.load(pickle_in)

st.set_page_config(page_title='Airline Passenger Satisfaction', layout='centered', initial_sidebar_state = 'expanded')

# Custom CSS styles
st.markdown("""
    <style>
    .title {
        font-size: 35px;
        font-family: Arial, sans-serif;
        background-color: #0728ad;
        color:white; 
        text-align: center;
        marging-top:0;
        margin-bottom:20px;    
        padding:4px;
        font-weight:bold;
        border-radius: 10px;
    }
    .header1{
        font-size: 25px;
        font-weight: bold;
        border-bottom:1px solid gray;
        margin-top:10px
        margin-bottom:10px;
        padding-bottom:4px;
    }
    @media screen and (max-width: 600px) {
        .title {
            font-size: 22px; /* Adjust the font size for small devices */
        }
        .header1{
            font-size:18px;
        }
    }
    </style>
""", unsafe_allow_html=True)

sidebar_css = """
<style>
.sidebar-content {
    padding: 0px;
}
.sidebar-header {
    font-size: 20px;
    font-weight: bold;
    margin-bottom: 20px;
}
.sidebar-image {
    max-width: 100%;
    border-radius: 10px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    margin-bottom: 20px;
}
.header-info {
    font-size: 16px;
    margin-bottom: 10px;
}
</style>
"""

st.markdown(sidebar_css, unsafe_allow_html=True)
st.sidebar.title("Project Information")
st.sidebar.markdown("""
    <div class="sidebar-content">
        <div class="sidebar-header">Airline Passenger Satisfaction Prediction Project</div>
        <p>This Streamlit app predicts airline passenger satisfaction using machine learning.</p>
        <p>Fill in the passenger details and rate your experience to see the prediction.</p>
    </div>
    <div class="header-info">
            The model considers various factors such as flight distance, service ratings, and passenger demographics.
""", unsafe_allow_html=True)

st.sidebar.markdown("### Useful Links")
st.sidebar.markdown("- [GitHub Repository](https://github.com/navadkarsujit/Airline-Passenger-Satisfaction-ML-Project)")
st.sidebar.markdown("### Contributors")
st.sidebar.markdown("* Sujit Navadkar")

st.markdown('<div class="title">Airline Passenger Satisfaction <br> Prediction</div>', unsafe_allow_html=True)

def main():
    with st.container(border=True):
        st.markdown('<div class="header1">Passenger Details</div>', unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            Gender = st.radio("Gender",
                            ["Male", "Female"],
                            index=None,
                            horizontal=True)
        with col2:
            CustomerType = st.radio("Passanger is Regular",
                            ["Yes", "No"],
                            index=None,
                            horizontal=True)
        
        TravelType = st.radio("Type of Travel",
                            ["Personal", "Business"],
                            index=None,
                            horizontal=True)
        
        col1, col2= st.columns(2)
        with col2:
            Classt = st.selectbox("Class",
                                ("Eco", "Eco Plus", "Business"),
                                index=None,
                                placeholder="Select Class",)
        with col1:
            Age = st.number_input('Age',min_value=7,value=None,placeholder="Enter Age")
        with col2:
            FlightDistance = st.number_input('Flight Distance',min_value=30,value=None,placeholder="Enter Distance")
        with col1:
            ArrivalDelay=st.number_input('Arrival Delay in Minutes')

    with st.container(border=True):

        st.markdown('<div class="header1">Please rate your experience (from 1 to 5 stars)</div>', unsafe_allow_html=True)
        col1, col2, col3, col4=st.columns(4)
        with col1:
            wifi = st.radio("Wifi Service",
                            [1, 2, 3, 4, 5],
                            index=None,
                            horizontal=True)
        with col2:
            OnlineBook = st.radio("Online Booking",
                            [1, 2, 3, 4, 5],
                            index=None,
                            horizontal=True)
        with col3:
            timeconvenient = st.radio("Time convenient",
                            [1, 2, 3, 4, 5],
                            index=None,
                            horizontal=True)
        with col4:
            Food = st.radio("Food and Drink",
                            [1, 2, 3, 4, 5],
                            index=None,
                            horizontal=True)
        with col1:
            Onlineboarding = st.radio("Online Boarding",
                            [1, 2, 3, 4, 5],
                            index=None,
                            horizontal=True)
        with col2:
            Seatcomfort = st.radio("Seat Comfort",
                            [1, 2, 3, 4, 5],
                            index=None,
                            horizontal=True)
        with col3:
            Inflightentertainment = st.radio("Inflight Entertainment",
                            [1, 2, 3, 4, 5],
                            index=None,
                            horizontal=True)
        with col4:
            Onboardservice = st.radio("On-board Service",
                            [1, 2, 3, 4, 5],
                            index=None,
                            horizontal=True)
        with col1:
            Legroomservice = st.radio("Leg Room",
                            [1, 2, 3, 4, 5],
                            index=None,
                            horizontal=True)
        with col2:
            Baggagehandling = st.radio("Baggage Handling",
                            [1, 2, 3, 4, 5],
                            index=None,
                            horizontal=True)
        with col3:
            Checkinservice = st.radio("Checkin Service",
                            [1, 2, 3, 4, 5],
                            index=None,
                            horizontal=True)
        with col4:
            Inflightservice = st.radio("Inflight Service",
                            [1, 2, 3, 4, 5],
                            index=None,
                            horizontal=True)
        with col1:
            Cleanliness = st.radio("Cleanliness",
                            [1, 2, 3, 4, 5],
                            index=None,
                            horizontal=True)
        with col2:
            Gatelocation = st.radio("Gate location",
                            [1, 2, 3, 4, 5],
                            index=None,
                            horizontal=True)
            
    st.markdown('<div class="header1"></div>', unsafe_allow_html=True)

    with st.container():
        Button= st.button("Show Result",type='primary')
    
    sum=0
    count=0
    if Button:
        for i in [wifi, Classt, CustomerType, Gender, ArrivalDelay, timeconvenient, OnlineBook, 
                  Onlineboarding, Food, Seatcomfort, Inflightentertainment, Onboardservice, 
                  Legroomservice, Gatelocation, Inflightservice, Baggagehandling, Checkinservice, Cleanliness, TravelType]:
            if i is None:
                count=count+1
            else:
                sum=sum+1
        if count!=0:
            st.error("Please select all fields")
    
        if FlightDistance==None:
            st.error("Enter Distance")
        else:
            sum=sum+1

        if Age==None:
            st.error("Enter Age")
        else:
            sum=sum+1
        
        # encoding
        classencode=None
        if Classt=="Business":
            classencode=0
        elif Classt=="Eco":
            classencode=1
        elif Classt=="Eco Plus":
            classencode=2

        genderencode=None
        if Gender=="Male":
            genderencode=1
        elif Gender=="Female":
            genderencode=0

        CustomerTypeEncode=None
        if CustomerType=="Yes":
            CustomerTypeEncode=0
        elif CustomerType=="No":
            CustomerTypeEncode=1

        TravalTypeEncode=None
        if TravelType=="Personal":
            TravalTypeEncode=1
        elif TravelType=="Business":
            TravalTypeEncode=0

        if sum==21:
            # normalize
            fdist=np.sqrt(FlightDistance)
            
            data=np.array([[Age,classencode,fdist,wifi,timeconvenient,OnlineBook,Gatelocation,Food,Onlineboarding,Seatcomfort,Inflightentertainment,Onboardservice,Legroomservice,Baggagehandling,Checkinservice,Inflightservice,Cleanliness,ArrivalDelay,genderencode,CustomerTypeEncode,TravalTypeEncode]])
            # scaling
            scalingdata=scaling.transform(data)

            # prediction
            report=LRmodel.predict(scalingdata)
            if report==1:
                st.success("Congratulations! The passenger is highly satisfied with the airline service.")
            elif report==0:
                st.warning("The passenger's opinion of the airline is either neutral or dissatisfied")
                st.warning("The airline service needs improvement.")


if __name__=='__main__':
    main()

        # l1=[wifi, Classt, CustomerType, Gender, ArrivalDelay, Age, timeconvenient, OnlineBook,
        #     Onlineboarding, Food, Seatcomfort, Inflightentertainment, Onboardservice, FlightDistance, 
        #     Legroomservice, Gatelocation, Inflightservice, Baggagehandling, Checkinservice, Cleanliness,TravelType]
        # l2=["wifi", "Class", "CustomerType", "Gender", "ArrivalDelay", "Age", "timeconvenient", "OnlineBook", 
        #  "Onlineboarding", "Food", "Seatcomfort", "Inflightentertainment", "Onboardservice", "FlightDistance", 
        #  "Legroomservice", "Gatelocation", "Inflightservice", "Baggagehandling", "Checkinservice", "Cleanliness","TravelType"]
        # for j,k in zip(l1,l2):
        #     st.write(k," : ",j)

        # st.write(Age,Classt,FlightDistance,wifi,timeconvenient,OnlineBook,Gatelocation,Food,Onlineboarding,Seatcomfort,Inflightentertainment,Onboardservice,Legroomservice,Baggagehandling,Checkinservice,Inflightservice,Cleanliness,ArrivalDelay,Gender,CustomerType,TravelType)
        # st.write(Age,classencode,fdist,wifi,timeconvenient,OnlineBook,Gatelocation,Food,Onlineboarding,Seatcomfort,Inflightentertainment,Onboardservice,Legroomservice,Baggagehandling,Checkinservice,Inflightservice,Cleanliness,ArrivalDelay,genderencode,CustomerTypeEncode,TravalTypeEncode)
        
        # #python -m streamlit run app.py