"""
Engineering Vision Analysis Module
Specialized computer vision tools for analyzing engineering projects
"""

import cv2
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from ultralytics import YOLO
import base64
import io

class EngineeringVisionAnalyzer:
    def __init__(self):
        self.yolo_model = None
        self.load_models()
    
    def load_models(self):
        """Load YOLO model for component detection"""
        try:
            print("⏳ Loading YOLO model for engineering components...")
            self.yolo_model = YOLO('yolov8n.pt')
            print("✅ YOLO model loaded successfully")
        except Exception as e:
            print(f"⚠️ Could not load YOLO model: {e}")
            self.yolo_model = None
    
    def detect_components(self, frame):
        """Detect engineering components in the frame"""
        if self.yolo_model is None:
            return []
        
        results = self.yolo_model(frame)
        detections = []
        
        for result in results:
            boxes = result.boxes
            if boxes is not None:
                for box in boxes:
                    cls = int(box.cls[0])
                    conf = float(box.conf[0])
                    class_name = self.yolo_model.names[cls]
                    bbox = box.xyxy[0].cpu().numpy()
                    
                    detections.append({
                        'class': class_name,
                        'confidence': conf,
                        'bbox': bbox,
                        'center': [(bbox[0] + bbox[2])/2, (bbox[1] + bbox[3])/2]
                    })
        
        return detections
    
    def analyze_wiring_patterns(self, frame):
        """Analyze wiring patterns for common errors"""
        # Convert to grayscale for edge detection
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Detect edges
        edges = cv2.Canny(gray, 50, 150)
        
        # Find lines (potential wires)
        lines = cv2.HoughLinesP(edges, 1, np.pi/180, threshold=50, 
                               minLineLength=30, maxLineGap=10)
        
        wiring_analysis = {
            'total_lines': 0,
            'horizontal_lines': 0,
            'vertical_lines': 0,
            'potential_crossings': 0
        }
        
        if lines is not None:
            wiring_analysis['total_lines'] = len(lines)
            
            for line in lines:
                x1, y1, x2, y2 = line[0]
                
                # Determine line orientation
                if abs(x2 - x1) > abs(y2 - y1):
                    wiring_analysis['horizontal_lines'] += 1
                else:
                    wiring_analysis['vertical_lines'] += 1
        
        return wiring_analysis
    
    def detect_color_components(self, frame):
        """Detect components by color (resistors, capacitors, etc.)"""
        # Convert to HSV for better color detection
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        # Define color ranges for common components
        color_ranges = {
            'red_resistor': ([0, 100, 100], [10, 255, 255]),
            'brown_resistor': ([10, 100, 20], [20, 255, 200]),
            'green_capacitor': ([40, 40, 40], [80, 255, 255]),
            'blue_ic': ([100, 50, 50], [130, 255, 255])
        }
        
        color_detections = {}
        
        for component, (lower, upper) in color_ranges.items():
            mask = cv2.inRange(hsv, np.array(lower), np.array(upper))
            contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            
            # Filter contours by area
            valid_contours = [c for c in contours if cv2.contourArea(c) > 100]
            color_detections[component] = len(valid_contours)
        
        return color_detections
    
    def create_analysis_report(self, frame, detections, wiring_analysis, color_detections):
        """Create a comprehensive analysis report"""
        report = {
            'total_components': len(detections),
            'component_types': {},
            'wiring_analysis': wiring_analysis,
            'color_analysis': color_detections,
            'potential_issues': []
        }
        
        # Count component types
        for detection in detections:
            comp_type = detection['class']
            if comp_type in report['component_types']:
                report['component_types'][comp_type] += 1
            else:
                report['component_types'][comp_type] = 1
        
        # Identify potential issues
        if wiring_analysis['total_lines'] < 5:
            report['potential_issues'].append("Very few wiring connections detected - check for loose wires")
        
        if wiring_analysis['potential_crossings'] > 10:
            report['potential_issues'].append("Many wire crossings detected - potential short circuit risk")
        
        if len(detections) < 3:
            report['potential_issues'].append("Very few components detected - ensure all components are visible")
        
        return report
    
    def encode_image(self, image):
        """Convert PIL image to base64 string"""
        if isinstance(image, np.ndarray):
            image = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        
        buffered = io.BytesIO()
        image.save(buffered, format="JPEG")
        img_str = base64.b64encode(buffered.getvalue()).decode()
        return img_str
    
    def create_enhanced_prompt(self, frame, user_query="", analysis_report=None):
        """Create an enhanced prompt with detailed analysis"""
        base64_image = self.encode_image(frame)
        
        # Add analysis report to prompt if available
        analysis_text = ""
        if analysis_report:
            analysis_text = f"""
DETECTED COMPONENTS: {analysis_report['total_components']}
COMPONENT TYPES: {analysis_report['component_types']}
WIRING ANALYSIS: {analysis_report['wiring_analysis']}
COLOR DETECTIONS: {analysis_report['color_analysis']}
POTENTIAL ISSUES: {analysis_report['potential_issues']}
"""
        
        prompt = f"""You are Jarvis, an expert engineering diagnostic assistant with advanced computer vision capabilities. 
Analyze this image of an engineering project and provide detailed technical feedback.

USER QUERY: {user_query if user_query else "Please analyze this engineering project and identify any issues or improvements needed."}

{analysis_text}

ANALYSIS REQUIREMENTS:
1. Identify all visible components (resistors, capacitors, wires, ICs, breadboard connections, etc.)
2. Check for common wiring errors (wrong pin connections, loose wires, incorrect component placement)
3. Verify component orientation and polarity
4. Look for potential short circuits, open circuits, or incorrect connections
5. Analyze breadboard connections for proper row/column alignment
6. Check for missing components or incorrect component values
7. Suggest specific improvements or corrections
8. Provide actionable advice for fixing any issues

Please be thorough and technical in your analysis. If you spot specific issues like "wire connected to A4 should be A3" or "resistor R1 is in wrong orientation", clearly state the problem and exact solution."""

        return prompt, base64_image

# Example usage
if __name__ == "__main__":
    analyzer = EngineeringVisionAnalyzer()
    print("✅ Engineering Vision Analyzer initialized")
