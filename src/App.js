import React from "react";
import { useEffect, useState } from "react";
import { Map, GoogleApiWrapper, Marker } from "google-maps-react";
import { getCoordinates } from "./getCoordinates";
import data from "./assets/data.json";

const mapStyles = {
  width: "100%",
  height: "100%",
};

const App = (props) => {
  const [deals, setDeals] = useState([]);

  useEffect(() => {
    const fetchDealsData = async () => {
      if (process.env.REACT_APP_ENV === "development") {
        await updateDeals();
      } else setDeals(data);
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

  return (
    <div>
      <Map
        google={props.google}
        zoom={13}
        style={mapStyles}
        initialCenter={{ lat: 48.864716, lng: 2.344024 }}
      >
        {deals.map((deal, index) => (
          <Marker key={index} position={{ lat: deal.coordinates.lat, lng: deal.coordinates.lng }} />
        ))}
      </Map>
    </div>
  );
};

export default GoogleApiWrapper({
  apiKey: process.env.REACT_APP_GOOGLE_MAPS_API_KEY,
})(App);
