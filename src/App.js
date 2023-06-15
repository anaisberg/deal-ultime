import React from "react";
import { useEffect } from "react";
import { Map, GoogleApiWrapper, Marker } from "google-maps-react";

const mapStyles = {
  width: "100%",
  height: "100%",
};

const App = (props) => {
  //   const [deals, setDeals] = useState([]);
  //   const currentUrl = window.location.href;
  //   const endpoint = `${currentUrl}getlocations`;
  useEffect(() => {
    fetch("http://localhost:5000/getlocations", {
      methods: "GET",
      headers: {
        "Content-Type": "application/json",
      },
    }).then((response) => {
      console.log(response.body);
      // initMap(response.body);
    });
  }, []);

  return (
    <div>
      <Map
        google={props.google}
        zoom={10}
        style={mapStyles}
        initialCenter={{ lat: 48.864716, lng: 2.349014 }}
      >
        <Marker position={{ lat: 48.0, lng: -122.0 }} />
      </Map>
    </div>
  );
};

export default GoogleApiWrapper({
  apiKey: process.env.REACT_APP_GOOGLE_MAPS_API_KEY,
})(App);
