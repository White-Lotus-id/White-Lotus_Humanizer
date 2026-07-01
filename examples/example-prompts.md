# Example Prompts

Real-world usage examples for the humanize skill.

---

## 1. Generate a fresh Introduction section

```
[SECTION INTAKE]

1. Thesis Title/Topic: Development of a Brownout Guard System for Residential Power
   Monitoring in ALECO Service Territory
2. Thesis Category: Development
3. Section/Part: Introduction
4. Voice Target: VOICE-A
5. References:
   - Santos, J. R., & Cruz, M. A. (2022). Power quality in Philippine distribution
     networks. Journal of Electrical Engineering Philippines, 14(2), 45-58.
     https://doi.org/10.xxxx/xxxx
   - ALECO. (2023). Annual service reliability report. Albay Electric Cooperative.
   - Dela Cruz, P. B. (2021). Voltage monitoring systems for rural electrification.
     Philippine Institute of Electrical Engineers Journal, 8(1), 12-24.
   - Reyes, L. C., & Torres, A. M. (2020). Household appliance damage from
     undervoltage events in Bicol Region. Energy Research Philippines, 5(3), 88-102.
   - Garcia, R. F. (2023). Smart home power monitoring solutions. IEEE Access,
     11, 24531-24545. https://doi.org/10.1109/ACCESS.2023.xxxxx

[CONFIRMED: Generate Introduction]
```

---

## 2. Humanize an existing AI-written paragraph

```
Humanize this:

The proposed system integrates a voltage sensor with a microcontroller to
monitor power quality in real-time. The system utilizes the PZEM-004T module
which enables accurate measurement of voltage, current, and power factor.
Furthermore, the data is transmitted wirelessly to a mobile application,
thereby providing users with immediate notifications when voltage drops below
the acceptable threshold of 0.90 per unit. This demonstrates the system's
capability to address the significant issue of undervoltage events that affect
household appliances.

Voice Target: VOICE-B
Thesis Category: Development
Section: Research Design
```

---

## 3. Generate RRL with Theme Map

```
[SECTION INTAKE]

1. Thesis Title/Topic: Automated Rice Seed Viability Detection Using Infrared
   Thermography and Convolutional Neural Networks
2. Thesis Category: Development
3. Section/Part: RRL — Theme: Infrared Thermography in Agriculture
4. Voice Target: VOICE-A
5. References:
   - Mancini, M., & Lopez, F. (2022). Infrared imaging for crop quality assessment.
     Biosystems Engineering, 218, 45-56.
   - Kim, S., Park, J., & Lee, H. (2021). Thermal imaging for seed germination
     prediction. Journal of Agricultural Engineering, 58(3), 112-124.
   - Nguyen, T. (2023). Non-destructive methods for rice quality evaluation.
     Computers and Electronics in Agriculture, 205, 107-119.

6. Theme Map:
   Theme 1: Infrared Thermography — Mancini & Lopez (2022), Nguyen (2023)
   Theme 2: Seed Viability Assessment Methods — Kim et al. (2021)

[THESIS ANCHOR]
Title: Automated Rice Seed Viability Detection Using Infrared Thermography and CNN
Category: Development
General Objective: To develop a non-destructive rice seed viability detection
system using infrared thermography and convolutional neural networks
Scope: Covers detection of rice seed viability using thermal images and
CNN classification only, limited to Maligaya variety
Key methodology: Image acquisition using FLIR thermal camera, CNN classification
using EfficientNet-B0

[CONFIRMED: Generate RRL — Theme: Infrared Thermography]
```

---

## 4. Convert BULLET EXPORT from /thesis-writer

```
Voice Target: VOICE-B
Section: Chapter 3 — Data Gathering Procedure
Thesis Category: Development

[BULLET EXPORT FROM THESIS-WRITER]
- Phase 1: Requirement Gathering
  - Interview stakeholders (household owners, ALECO technicians)
  - Identify voltage thresholds and monitoring frequency requirements
  - Review existing brownout incident reports from ALECO
- Phase 2: System Development
  - Hardware assembly: ESP32 + PZEM-004T + relay module
  - Firmware: FreeRTOS task scheduling for sensor polling
  - Mobile app: React Native with Firebase real-time database
- Phase 3: Testing and Evaluation
  - Unit testing of individual sensors
  - Integration testing of full system
  - User acceptance testing with 5 household owners in Polangui

[THESIS ANCHOR]
Title: Brownout Guard: A Residential Power Monitoring System for ALECO Service Territory
Category: Development
General Objective: To develop a residential power monitoring and protection system
Scope: Limited to monitoring voltage and current at the household level in ALECO
service territory, Polangui, Albay
Key methodology: RAD methodology, ESP32-based hardware, FreeRTOS firmware,
React Native mobile app
```

---

## 5. Request voice calibration from writing sample

```
[SECTION INTAKE]

1. Thesis Title/Topic: Salikchick Egg Incubation Monitoring System
2. Thesis Category: Development
3. Section/Part: Chapter 1 — Significance
4. Voice Target: VOICE-B

My writing sample (for calibration):
"This study is important because it helps poultry farmers monitor their
eggs better. The system will give them notifications so they don't have
to check manually. Because of that, they can focus on other things
and still make sure the incubation is going well."

5. References: [none needed for Significance]
```
