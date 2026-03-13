"use client";

interface Props {
  risk: number;
}

export default function RiskMeter({ risk }: Props) {
  let color = "green";
  let message = "Low Risk";

  if (risk > 70) {
    color = "red";
    message = "⚠️ High Risk: Possible Scam";
  } else if (risk > 40) {
    color = "orange";
    message = "⚠️ Medium Risk";
  }

  return (
    <div style={{ marginTop: "1rem" }}>
      <h3>📊 Scam Risk: {risk}%</h3>
      <div
        style={{
          width: "100%",
          height: "20px",
          background: "#ddd",
          borderRadius: "10px",
        }}
      >
        <div
          style={{
            width: `${risk}%`,
            height: "100%",
            background: color,
            borderRadius: "10px",
          }}
        />
      </div>
      <p style={{ color, fontWeight: "bold" }}>{message}</p>
    </div>
  );
}
