import React, { useEffect, useState } from "react";
import { View, Text, FlatList } from "react-native";
import { getPredictions } from "./api";

export default function App() {
  const [data, setData] = useState([]);

  useEffect(() => {
    getPredictions().then(setData);
  }, []);

  return (
    <FlatList
      data={data}
      keyExtractor={(item) => item.match}
      renderItem={({ item }) => (
        <View>
          <Text>{item.match}</Text>
          <Text>BTTS: {item.probability}</Text>
          <Text>EV: {item.ev}</Text>
        </View>
      )}
    />
  );
}
