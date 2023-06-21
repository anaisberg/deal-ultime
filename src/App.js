import React from "react";
import { useEffect, useState } from "react";
import { Map, GoogleApiWrapper, Marker } from "google-maps-react";
import { getCoordinates } from "./getCoordinates";

const mapStyles = {
  width: "100%",
  height: "100%",
};

const App = (props) => {
  const [deals, setDeals] = useState([]);
  //   const currentUrl = window.location.href;
  //   const endpoint = `${currentUrl}getlocations`;

  useEffect(() => {
    const fetchDealsData = async () => {
      if (process.env.REACT_APP_ENV === "development") {
        const updatedDeals = await updateDeals();
        setDeals(updatedDeals);
      } else setDeals();
    };
    fetchDealsData();
  }, []);

  const updateDeals = async () => {
    const updatedDeals = await fetch("http://localhost:3000/getlocations", {
      method: "GET",
      crossorigin: true,
    }).then((response) => response.json());

    const updatedDealsWithCoordinates = Promise.all(
      updatedDeals.map(async (deal) => {
        const coordinates = await getCoordinates(deal.address);
        return {
          ...deal,
          coordinates,
        };
      })
    );
    setDeals(updatedDealsWithCoordinates);
  };

  console.log(deals);

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
