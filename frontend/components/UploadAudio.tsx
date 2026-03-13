"use client";

interface Props {
  setResult: Function;
  setLoading: Function;
}

export default function UploadAudio({ setResult, setLoading }: Props) {
  const BACKEND_URL = "https://YOUR_BACKEND_URL/analyze";

  const handleUpload = async (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (!file) return;

    setLoading(true);

    const formData = new FormData();
    formData.append("file", file);

    try {
      const res = await fetch(BACKEND_URL, {
        method: "POST",
        body: formData,
      });

      if (!res.ok) throw new Error("Backend error");

      const data = await res.json();
      setResult(data);
    } catch (err) {
      alert("Error connecting to backend");
      console.error(err);
    }

    setLoading(false);
  };

  return (
    <div style={{ margin: "1rem 0" }}>
      <input type="file" accept="audio/*" onChange={handleUpload} />
    </div>
  );
}
