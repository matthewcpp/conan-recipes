#define EZMIDI_IMPLEMENTATION
#include <ezmidi/ezmidi.h>


int main(int argc, char** argv) {

    Ezmidi_Context* ezmidi = ezmidi_create(nullptr);
    int32_t count = ezmidi_get_source_count(ezmidi);
    ezmidi_destroy(ezmidi);

    return 0;
}
