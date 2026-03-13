import "./globals.css";

export const metadata = {
  title: "DhvaniKavach",
  description: "Scam Call Detection System",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
