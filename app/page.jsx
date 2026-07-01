// Frontend Dashboard Code (Next.js / React)
// File: page.jsx (or App.jsx)
"use client";

import React, { useState, useEffect } from 'react';
import { Camera, CheckCircle, XCircle, Activity, ShieldCheck, Car, Scan, ArrowRight, FileText, Download } from 'lucide-react';

// आपका लाइव Render API URL
const API_BASE_URL = "https://ai-vehicle-inspection.onrender.com";

export default function Dashboard() {
  const [view, setView] = useState('dashboard'); // 'dashboard', 'inspection', 'report'
  const [reportData, setReportData] = useState(null);
  const [isProcessing, setIsProcessing] = useState(false);
  const [liveStream, setLiveStream] = useState(null);

  // डमी गाड़ी जो कतार (Queue) में है
  const activeVehicle = {
    vin: "WBA00000000000000",
    plate_number: "KSA 1234",
    sequence_number: "99887766",
    make: "Toyota Hilux",
    model_year: 2024,
    vehicle_type: "truck"
  };

  // WebSocket से लाइव जुड़ने क��� फंक्शन
  useEffect(() => {
    if (view === 'inspection') {
      const ws = new WebSocket(`wss://ai-vehicle-inspection.onrender.com/ws/inspect/TEST-123`);
      
      ws.onopen = () => console.log("WebSocket Connected!");
      ws.onmessage = (event) => {
        const data = JSON.parse(event.data);
        setLiveStream(data);
      };
      
      // हर सेकंड डमी डेटा भेजना ताकि सर्वर जवाब दे (Simulation)
      const interval = setInterval(() => {
        if(ws.readyState === WebSocket.OPEN) ws.send("heartbeat");
      }, 1000);

      return () => {
        clearInterval(interval);
        ws.close();
      };
    }
  }, [view]);

  // FastAPI बैकएंड से रिपोर्ट मंगाने का फंक्शन
  const generateFinalReport = async () => {
    setIsProcessing(true);
    try {
      const payload = {
        ...activeVehicle,
        side_slip_val: 4.5,
        brake_efficiency_val: 52.0,
        brake_imbalance_val: 12.5,
        front_barrier_height_val: 450.0,
        rear_barrier_height_val: 520.0,
        side_barrier_gap_val: 280.0,
        side_barrier_height_val: 510.0,
        tire_tread_depth_val: 2.5,
        oil_leakage_detected: false
      };

      const response = await fetch(`${API_BASE_URL}/api/v1/inspect/process`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload)
      });

      const data = await response.json();
      setReportData(data);
      setView('report');
    } catch (error) {
      console.error("API Error:", error);
      alert("Backend API से कनेक्ट नहीं हो पा रहा है। क्या आपका रेंडर सर्वर Running है?");
    }
    setIsProcessing(false);
  };

  // -------------------------------------------------------------
  // 1. DASHBOARD VIEW
  // -------------------------------------------------------------
  const renderDashboard = () => (
    <div className="p-8 space-y-6">
      <div className="flex justify-between items-center">
        <h1 className="text-3xl font-bold text-slate-800">Command Center</h1>
        <div className="bg-blue-100 text-blue-800 px-4 py-2 rounded-full font-bold flex items-center gap-2">
          <Activity size={18} /> API Connected
        </div>
      </div>

      <div className="bg-white rounded-xl shadow-md border border-slate-200 overflow-hidden">
        <div className="bg-slate-50 px-6 py-4 border-b border-slate-200 flex items-center gap-2">
          <Scan size={20} className="text-slate-500" />
          <h3 className="font-bold text-slate-700">Vehicle Queue</h3>
        </div>
        <table className="w-full text-left">
          <thead className="bg-slate-50 text-slate-500 text-sm">
            <tr>
              <th className="px-6 py-3">Plate Number</th>
              <th className="px-6 py-3">Make / Model</th>
              <th className="px-6 py-3">Type</th>
              <th className="px-6 py-3">Action</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-slate-100">
            <tr className="hover:bg-slate-50">
              <td className="px-6 py-4 font-bold text-lg">{activeVehicle.plate_number}</td>
              <td className="px-6 py-4 text-slate-600">{activeVehicle.make} ({activeVehicle.model_year})</td>
              <td className="px-6 py-4 uppercase font-semibold text-xs text-slate-500">{activeVehicle.vehicle_type}</td>
              <td className="px-6 py-4">
                <button 
                  onClick={() => setView('inspection')}
                  className="bg-slate-900 text-white px-4 py-2 rounded-lg text-sm font-bold hover:bg-indigo-600 transition"
                >
                  Start AI Inspection
                </button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  );

  // -------------------------------------------------------------
  // 2. LIVE INSPECTION BAY VIEW
  // -------------------------------------------------------------
  const renderInspectionBay = () => (
    <div className="p-6 h-[calc(100vh-4rem)] bg-slate-900 text-white flex flex-col">
      <div className="flex justify-between items-center mb-6">
        <h2 className="text-2xl font-bold flex items-center gap-3">
          <Camera className="text-indigo-400" /> Live Vision AI (SASO Scanner)
        </h2>
        {liveStream ? (
          <span className="bg-green-500/20 text-green-400 px-3 py-1 rounded-full text-sm font-mono border border-green-500/30 flex items-center gap-2">
            <span className="w-2 h-2 bg-green-400 rounded-full animate-pulse"></span>
            WS: LIVE | {liveStream.fps} FPS
          </span>
        ) : (
          <span className="text-slate-400 text-sm font-mono">Connecting WebSocket...</span>
        )}
      </div>

      <div className="flex-1 border-2 border-slate-700 rounded-lg bg-black relative overflow-hidden flex items-center justify-center mb-6 shadow-2xl">
        <div className="absolute top-4 left-4 text-xs font-mono bg-black/60 px-2 py-1 rounded">
          {liveStream ? liveStream.active_camera_node : 'Camera Output'}
        </div>
        
        {/* Simulated AI Bounding Box */}
        <div className="w-64 h-48 border-2 border-green-500 bg-green-500/10 relative">
          <span className="absolute -top-6 left-[-2px] bg-green-500 text-black text-[10px] px-1 font-bold">
            Side_Guard_Detected {liveStream ? liveStream.ai_confidence_average : '0.0'}
          </span>
        </div>
      </div>

      <button 
        onClick={generateFinalReport}
        disabled={isProcessing}
        className="w-full bg-indigo-600 text-white py-4 rounded-xl font-bold text-lg hover:bg-indigo-500 transition shadow-lg disabled:opacity-50"
      >
        {isProcessing ? 'Processing SASO Metrics...' : 'Complete Inspection & Generate Report'}
      </button>
    </div>
  );

  // -------------------------------------------------------------
  // 3. FINAL REPORT VIEW
  // -------------------------------------------------------------
  const renderReport = () => {
    if (!reportData) return null;
    const isPass = reportData.decision.status === 'PASS';

    return (
      <div className="p-8 bg-slate-100 min-h-screen flex justify-center">
        <div className="bg-white w-full max-w-4xl shadow-2xl rounded-xl overflow-hidden border border-slate-200">
          {/* Header */}
          <div className="bg-slate-900 text-white p-8 flex justify-between items-center">
            <div>
              <h1 className="text-3xl font-bold">Official SASO Inspection Report</h1>
              <p className="text-slate-400 mt-1">Vehicle Compliance Center</p>
            </div>
            <div className="text-right">
              <div className="text-sm text-slate-400 font-mono">ID: {reportData.inspection_id}</div>
              <div className="font-mono text-sm">{new Date(reportData.timestamp).toLocaleString()}</div>
            </div>
          </div>

          {/* Result Block */}
          <div className="p-8 border-b border-slate-200 flex justify-between items-center bg-slate-50">
            <div>
              <p className="text-sm text-slate-500 uppercase font-bold tracking-widest">Plate Number</p>
              <p className="text-3xl font-black font-mono mt-1">{reportData.vehicle.plate_number}</p>
            </div>
            <div className={`px-8 py-4 rounded-2xl border-4 flex items-center gap-4 ${isPass ? 'bg-green-50 border-green-400 text-green-700' : 'bg-red-50 border-red-400 text-red-700'}`}>
              {isPass ? <CheckCircle size={40} /> : <XCircle size={40} />}
              <div>
                <div className="text-sm font-bold uppercase tracking-widest">Final Status</div>
                <div className="text-4xl font-black">{reportData.decision.status}</div>
              </div>
            </div>
          </div>

          {/* Components Validation */}
          <div className="p-8">
            <h3 className="text-xl font-bold text-slate-800 mb-6 border-b pb-2">SASO Standards Breakdown</h3>
            <div className="grid grid-cols-2 gap-4">
              {Object.entries(reportData.saso_validation).map(([key, data]) => (
                <div key={key} className="p-4 border rounded-lg bg-white flex justify-between items-center shadow-sm">
                  <div>
                    <div className="font-semibold text-slate-700 capitalize">{key.replace(/_/g, ' ')}</div>
                    <div className="text-xs font-mono text-slate-500 mt-1">Val: {data.value || data.gap_value || String(data.detected)}</div>
                  </div>
                  <span className={`px-3 py-1 rounded text-xs font-bold ${data.status === 'PASS' ? 'bg-green-100 text-green-700' : 'bg-red-100 text-red-700'}`}>
                    {data.status}
                  </span>
                </div>
              ))}
            </div>
          </div>

          {/* Footer Security */}
          <div className="p-6 bg-slate-50 border-t border-slate-200 flex justify-between items-center">
            <div className="text-xs text-slate-400 font-mono">
              <ShieldCheck size={14} className="inline mr-1" />
              Digital Signature: {reportData.security.digital_signature.slice(0, 20)}...
            </div>
            <button 
              onClick={() => setView('dashboard')}
              className="bg-slate-900 text-white px-6 py-2 rounded font-bold hover:bg-slate-800"
            >
              Back to Dashboard
            </button>
          </div>
        </div>
      </div>
    );
  };

  // -------------------------------------------------------------
  // MAIN RENDER (Header + Router)
  // -------------------------------------------------------------
  return (
    <div className="min-h-screen bg-slate-100 font-sans">
      <header className="bg-indigo-900 text-white h-16 flex items-center px-6 shadow-lg z-50 sticky top-0">
        <ShieldCheck className="text-indigo-400 mr-2" size={28} />
        <span className="text-xl font-black tracking-widest">
          SASO<span className="text-indigo-400">VISION</span>
        </span>
      </header>
      
      <main>
        {view === 'dashboard' && renderDashboard()}
        {view === 'inspection' && renderInspectionBay()}
        {view === 'report' && renderReport()}
      </main>
    </div>
  );
}
