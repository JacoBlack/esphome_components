#include "uart_mitm_uni.h"
#include "esphome/core/log.h"

namespace esphome {
namespace serial {

static const char *const TAG = "uart_mitm_uni";

void UARTMITMUNI::loop() {
  uint8_t c;
  while (this->uart_in_->available()) {
    this->uart_in_->read_byte(&c);
    this->uart_out_->write_byte(c);
  }
}

void UARTMITMUNI::dump_config() { ESP_LOGCONFIG(TAG, "UART MITM UNI"); }

}  // namespace serial
}  // namespace esphome
