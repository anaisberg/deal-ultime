export const getCoordinates = async (address) => {
  const response = await fetch(
    `https://maps.googleapis.com/maps/api/geocode/json?address=${address}&key=${process.env.REACT_APP_GOOGLE_MAPS_API_KEY}`
  );
  const data = await response.json();
  const location = data.results[0].geometry.location;
  return location;
};
