package ru.gmed.cms.db.repos;

import org.springframework.data.repository.CrudRepository;
import ru.gmed.cms.db.entity.Doctor;

import java.util.UUID;

public interface DoctorRepo extends CrudRepository<Doctor, UUID> {
}
